from django.conf.urls import patterns
from django.contrib import admin
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
import subprocess


def console(request):
    """
    Serves the console at /admin/console
    """
    if request.user.is_superuser:
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
