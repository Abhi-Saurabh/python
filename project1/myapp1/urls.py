from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello, name="hello"),
    path('get_emp', views.get_emp, name="get_emp"),
    path('get_emp_view', views.get_emps, name="get_emp_view"),
    path('form_submit', views.form_submit, name="form_submit"),
]