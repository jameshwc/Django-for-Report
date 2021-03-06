FROM ubuntu:18.04

RUN mkdir /mainpage
RUN mkdir /mainpage/logs
ADD . /mainpage/
WORKDIR /mainpage/
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    software-properties-common
RUN apt-get install -y python3.6 \
    python3.6-dev \
    python3-distutils \
    libmysqlclient-dev \
    gcc \
    build-essential \
    apache2 \ 
    libapache2-mod-wsgi-py3 \
    python-apt \
    unattended-upgrades \
    libcairo2-dev \
    wget \
    libssl-dev \
    libatlas-base-dev \
    git
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.6 get-pip.py
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
RUN pip3 install -r requirements.txt
RUN mv mainpage.conf /etc/apache2/sites-available/
RUN a2enmod wsgi
RUN a2ensite mainpage
RUN a2dissite 000-default.conf
EXPOSE 80
ENTRYPOINT service apache2 restart && bash
