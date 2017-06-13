'''
steps: to install
1.>mkdir django_practice   
>cd django_practice/
>ll
>mkdir dtl_test
>cd dtl_test/

2.to check django is present or not
>python
>import django      #no module named django

3.to install django
>pip install django

4.how to know which packages are installed in my lib
a)to go check library
b)>pip freeze > lib.txt
>vim lib.txt
>ll
>pip install -r lib.txt    #to install all library

steps:to know basics to create project
1.>django-admin startproject pro1     #to create a project
>ll                     #to see no of fies
>cd pro1/
>ll

2.to create an app in django
>python manage.py runserver
>python manage.py startapp mcq   #to start a project
>python manage.py runserver
>python manage.py createsuperuser   #user created
>python manage.py runserver
>python manage.py shell
>from django.contrib.auth.models import User

DTL:django template library

'''
