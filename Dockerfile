FROM python:3.7

ADD . .
RUN apt-get update && apt-get install -y python-apt unattended-upgrades libcairo2-dev
RUN pip3 install -r requirements.txt
RUN python3 manage.py test
EXPOSE 8000
ENTRYPOINT [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
