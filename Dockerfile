FROM python:3.12-slim

WORKDIR django_referral/

COPY requirements.txt /django_referral/

RUN pip install -r requirements.txt

COPY . /django_referral/

RUN ["chmod", "+x", "./docker-entrypoint.sh"]
ENTRYPOINT ["bash", "-c"]
CMD ["./docker-entrypoint.sh"]