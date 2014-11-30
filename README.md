![Django-Console](https://raw.githubusercontent.com/atmb4u/django-console/master/django-console/static/images/console-128x128.png) 

##Django-Console

bash console in the browser for django

Did a quick update on the code, and need to pull the code and restart the server? Django-Console is for you!

## Installation

**Step 1**
> pip install django-console

**Step 2**

include __django-console__ into INSTALLED_APPS ```settings.py```

```python
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
**Step 3**

run
> python manage.py collectstatic

##Screenshots

in your browser, goto

http://127.0.0.1:8000/admin/console/

![Django-Console](https://raw.githubusercontent.com/atmb4u/django-console/master/django-console/static/images/screenshot.png)

NB: make sure you got superuser privileges.


##Tip
To run sudo tasks, you can use

```bash
echo mypassword | sudo -S command
```

Example command 
```bash
echo pa$$w0rD | sudo -S service nginx restart
```

## License

BSD License - checkout LICENSE file for the complete license document


## Authors
[Anoop Thomas Mathew](https://twitter.com/atmb4u "atmb4u")
