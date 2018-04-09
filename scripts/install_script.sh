#!/bin/bash

brew install python
sudo pip3 install virtualenv

export WORK_ENV=~/.shukerbaker_virtualenvs
export WORK_ENV_ACTIVATE=~/.shukerbaker_virtualenvs/bin/activate
mkdir -p $WORK_ENV
sudo rm -rf $WORK_ENV
virtualenv $WORK_ENV
source $WORK_ENV_ACTIVATE

pip3 install Django==2.0.4
pip3 install mysqlclient==1.3.12
pip3 install mock==2.0.0
pip3 install freezegun==0.3.10
pip3 install pyflakes==1.6.0
pip3 install pep8==1.7.1
pip3 install requests==2.18.4
pip3 install ipython==6.3.1
pip3 install django-webpack-loader==0.6.0
pip3 install wheel==0.26.0

