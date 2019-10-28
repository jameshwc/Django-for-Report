FROM ubuntu:18.04

ADD . .
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    software-properties-common
RUN add-apt-repository ppa:jonathonf/python-3.6 && apt-get install -y python3.6 \
    python3.6-dev \
    python3-distutils \
    libmysqlclient-dev \
    gcc \
    apache2 \ 
    libapache2-mod-wsgi-py3 \
    python-apt \
    unattended-upgrades \
    libcairo2-dev \
    wget
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.6 get-pip.py
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
ENV PYTHONIOENCODING=utf-8
RUN pip3 install -r requirements.txt
RUN python3 manage.py test
EXPOSE 8000
ENTRYPOINT [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
