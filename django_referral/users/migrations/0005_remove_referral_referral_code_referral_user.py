# Generated by Django 5.1.3 on 2024-12-01 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_referral_referral_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referral',
            name='referral_code',
        ),
        migrations.AddField(
            model_name='referral',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
    ]
