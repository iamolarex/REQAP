# REQAP

A Multilevel request/approval system for institutions

## Installation

- clone the repo

``git clone https://github.com/aiomi/REQAP.git``

- Install requirements file

``pip3 install -r requirements.txt``

- Create a local_settings.py and update it accordingly

``cp main/settings/default_settings.py main/settings/local_settings.py``

- run migrations and start the server

``python manage.py migrate``

``python manage.py runserver``
