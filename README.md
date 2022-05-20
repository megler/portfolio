# Portfolio

A Django based personal Portfolio showcasing current work and projects

## Usage

In the terminal, change directory into `website` and run `python manage.py runserver`.

The app can now by run by pointing your browser to [localhost](http://127.0.0.1:8000/).

## Features

1. The homepage lists current projects broken into large and small.
2. Smaller Flask apps from my other repos have been converted into Django apps
to conserve Heroku instances.

# TODO's 


2. Convert Flask apps into Django apps
3. Roll out to production on Heroku 
4. remove EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" from line 23 in settings.py on roll to production.
