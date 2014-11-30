![Django-Console](https://raw.github.com/atmb4u/djano-console/master/django-console/static/images/console.png)
Django-Console
==============

bash console in the browser

## Installation

pip install django-console

include _django-console_ into INSTALLED_APPS ```settings.py```

```
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django-console'
)
```

##Screenshots

in your browser, goto

http://127.0.0.1:8000/admin/console/

![Django-Console](https://raw.github.com/atmb4u/djano-console/master/django-console/static/images/screeshot.png)

NB: make sure you got superuser privileges.


##Tip
To run sudo tasks, you can use

```
echo mypassword | sudo -S command
```

Eg: echo pa$$w0rD | sudo -S service nginx restart

## LICENSE

BSD License - checkout LICENSE file for the complete license document


