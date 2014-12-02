from django.conf.urls import patterns
from django.contrib import admin
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
import subprocess


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def console(request):
    """
    Serves the console at /admin/console
    SECURE_CONSOLE
        values: True/False
        Defined in settings to denote whether to allow access from http or https
        default: False - ALLOW access to ALL.
    CONSOLE_WHITELIST
        values: list of ip strings
        defines list of ips to be allowed
        default: ALLOW ALL ips unless defined.

    """
    try:
        v1 = request.is_secure() == settings.SECURE_CONSOLE
    except AttributeError:
        v1 = True
    try:
        v2 = get_client_ip(request) in settings.CONSOLE_WHITELIST
    except AttributeError:
        v2 = True
    except:
        print "CONSOLE_WHITELIST needs to be a list of ip addresses to be allowed access"
        v2 = True
    settings_variables = v1 and v2
    if request.user.is_superuser and settings_variables:
        context = {
            'STATIC_URL': settings.STATIC_URL
        }
        context.update(csrf(request))
        return render_to_response("django-console/admin/index.html", context)
    else:
        return HttpResponse("Unauthorized.", status=403)


def console_post(request):
    """
    Accepts POST requests from the web console, processes it and returns the result.
    """
    if request.user.is_superuser and request.POST:
        command = request.POST.get("command")
        if command:
            try:
                output = "%c(@olive)%" + subprocess.check_output(command, shell=True) + "%c()"
            except subprocess.CalledProcessError:
                output = "%c(@red)%Oh! I'm sorry. Something went wrong.%c()"
        else:
            output = "%c(@orange)%Try `ls` to start with.%c()"
        return HttpResponse(output)
    return HttpResponse("Unauthorized.", status=403)


def get_admin_urls(urls):
    """
    Appends the console and post urls to the url patterns
    """
    def get_urls():
        my_urls = patterns('',
                           (r'^console/$', admin.site.admin_view(console)),
                           (r'^console/post/$', admin.site.admin_view(console_post)))
        return my_urls + urls

    return get_urls


admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls
