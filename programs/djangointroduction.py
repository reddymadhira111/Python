'''
1.20 frameworks for python
django is highest level framework:tested,secured,efficient
the web framework for perfections with deadlines.
Django makes it easier to build better Web apps more quickly and with less code.


'''
'''
steps to install django:
1.whatever the operating system django installation process is same
>pip install Django==1.10.5
2. To start a project 
create a folder with name django-tutorial
open a command window with the same path
>django-admin startproject mysite
when click enter after this command django create a folder called mysite inside the django-tutorial
mysite->(mysite folder,manage.py)->mysite->(__init__.py,settings.py,urls.py,wsgi.py)
i)settings.py is more important.In that file installed apps 
every time you create an app u need to enter manually in the installed apps.
ii)urls.py:controller of the website
it contains url patterns->inside regular expressions
ex:urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
^:beginning of a string, $:end of a string
apps have their own urls.
3.>cd mysite
>python manage.py runserver
'''