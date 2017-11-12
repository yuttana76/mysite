# Useful Link
https://pythonspot.com/en/django-tutorial-building-a-note-taking-app/

https://www.fullstackpython.com/blog/python-3-django-gunicorn-linux-mint-17.html


# Django Getting started

https://pythonspot.com/en/tag/django/

https://tutorial.djangogirls.org/en/django_models/

# Django database model
python manage.py syncdb
instread
python manage.py migrate

# Static (config settings.py)
You shouldn't change BASE_DIR

Change STATIC_ROOT

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

And run collectstatic again
$python manage.py collectstatic

# Create admin user
$python manage.py createsuperuser

# Start django
$python manage.py runserver
$gunicorn mysite.wsgi

https://github.com/yuttana76/mysite.git

# Creating an application
1. Create application 
$ python manage.py startapp <app_name>

2. Modify setting.py by add

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '<app_name>',
]

2 Create model in
<app_name>/models.py

3 Create tables for models in your database
    -Django know that we have some changes in our model
    $ python manage.py makemigrations <app_name>

    -have to apply to our database
    $ python manage.py migrate <app_name>


# Django admin

To add, edit and delete the posts we've just modeled, we will use Django admin.

Let's open the blog/admin.py file and replace its contents with this:

blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)