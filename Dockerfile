FROM python:3.7

ADD . .
RUN apt-get -y install python-apt
RUN pip3 install -r requirements.txt
RUN python3 manage.py test
EXPOSE 8000
ENTRYPOINT [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
