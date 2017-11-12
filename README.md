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

