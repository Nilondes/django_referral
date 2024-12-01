from django.shortcuts import render, redirect
from .forms import PhoneForm, AuthNumberForm, ReferralCodeForm
from .models import User, Referral
from random import randint
from django.core.exceptions import ObjectDoesNotExist
from time import sleep


def authenticate(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            auth_number = randint(1000, 9999)
            sleep(2)
            try:
                user = User.objects.get(phone=phone)
            except ObjectDoesNotExist:
                referral_code = "".join([chr(randint(49, 123)) for _ in range(6)])
                user = User.objects.create(phone=phone, auth_number=auth_number, referral_code=referral_code)
            else:
                user.auth_number = auth_number
                user.save()
            return redirect('confirmation', user.pk)
    else:
        form = PhoneForm()
    return render(request, 'home.html', {'form': form})


def confirmation(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = AuthNumberForm(request.POST)
        if form.is_valid():
            auth_number = form.cleaned_data['auth_number']
            if auth_number == user.auth_number:
                return redirect('profile', user.pk)
            else:
                return redirect('home')
    else:
        form = AuthNumberForm()
        context = {'form': form, 'auth_number': user.auth_number}
    return render(request, 'confirmation.html', context)


def profile(request, pk):
    user = User.objects.get(pk=pk)
    context = {'referral_code': user.referral_code}
    if request.method == 'POST':
        form = ReferralCodeForm(request.POST)
        if form.is_valid():
            referral_code = form.cleaned_data['referral_code']
            try:
                referred_user = User.objects.get(referral_code=referral_code)
            except ObjectDoesNotExist:
                message = 'There is no such referral code in database!'
                context['form'] = form
            else:
                if referral_code == user.referral_code:
                    message = 'You cannot use your own referral code!'
                    context['form'] = form
                else:
                    referral = Referral.objects.create(user=referred_user, phone=user.phone)
                    message = 'You have added a referral code!'
                    context['referred_user'] = referred_user.referral_code
            context['message'] = message
            return render(request, 'profile.html', context)
    else:
        try:
            referral = Referral.objects.get(phone=user.phone)
        except ObjectDoesNotExist:
            form = ReferralCodeForm()
            context['form'] = form
        else:
            context['referred_user'] = referral.referral_code

    return render(request, 'profile.html', context)
