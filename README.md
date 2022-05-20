# Django API REST Framework - Installation Guide

**Official Website**

https://www.django-rest-framework.org/

----

# Requirements

* Python (3.6+)
* Django
* Python Venv

# Installation Guide

Install and create a virtual environment
    
    python3 -m pip install --user --upgrade pip
    python3 -m venv venv

Enter in virtual environment

    source venv/bin/activate

Install Django Rest Framework using `pip`

    pip install djangorestframework

To start a project,

    django-admin startproject example .

Migrate (create database), then create super user (admin), then build your api as you like

    python manage.py migrate
    python manage.py createsuperuser

# Usage

Here we'll see how to run the project and starting accessing the API

Put your 'asset_vulnerability.csv' csv file in main code folder.

Run server api
    
    python manage.py runserver

Load your csv file in

    http://127.0.0.1:8000/upload_csv

Login as admin with your previoulsy created superuser

    http://127.0.0.1:8000/admin

Use your api through

    http://127.0.0.1:8000/
