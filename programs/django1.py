'''
1.version
>python -m django --version
2.to create a project
>django-admin startproject mysite

manage.py: A command-line utility that lets you interact with this Django project in various ways.
The inner mysite/ directory is the actual Python package for your project. 
Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package
mysite/settings.py: Settings/configuration for this Django project
mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site
mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. 

3.verify your Django project works
>python manage.py runserver
If you want to change the server’s port:
>python manage.py runserver 8080
If you want to change the server’s IP:
>python manage.py runserver 0.0.0.0:8000

4.To create your app, make sure you’re in the same directory as manage.py and type this command:
>python manage.py startapp polls

'''

'''
1.Write your first view:Open the file polls/views.py 
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

2.To call the view, we need to map it to a URL - and for this we need a URLconf.
To create a URLconf in the polls directory, create a file called urls.py
polls/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

3.The next step is to point the root URLconf at the polls.urls module.
In mysite/urls.py, add an import for django.conf.urls.include and insert an include() in the urlpatterns list
mysite/urls.py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]

The url() function is passed four arguments, two required: regex and view, and two optional: kwargs, and name.
a)url() argument: regex
