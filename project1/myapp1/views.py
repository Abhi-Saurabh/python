from django.shortcuts import render
from . models import Post

# Create your views here.
from django.http import HttpResponse, response
from django.core import serializers

def hello(request):
    return HttpResponse('<h1>Hello!</h1>')

import json

def get_emp(request):
    student_list = Post.objects.filter(title='sdfgs',content='sdfg')
    # name = 'asdfasdf'
    # aa = ['w', '3',['asdlkfjalksd','asdkljfa']]
    # for student in student_list:
        # name = student
        # aa.append(name)
        # print(aa)
    data = serializers.serialize('json', student_list)
    return HttpResponse(data)

# import os

def get_emps(request):
    form = Post.objects.all()
    stu = {
            "student_number": form
        }
    # print(stu)
    # return HttpResponse(stu)
    #print(stu)
    #return HttpResponse(stu['student_number'][0])  
    return render(request, 'my_template_page.html',stu)


from django.contrib.auth.models import User

def form_submit(request):
    # LoginForm(request.POST)

    #form = ContactForm(request.POST)
    #print request.POST.get('email')
    #return HttpResponse(request.POST.get('email'))
    student_list = User.objects.filter(username=request.POST.get('email'))
    data = serializers.serialize('json', student_list)
    

    return HttpResponse(data)
		
    # return render(request, 'loggedin.html', {"username" : username})

# class LoginForm(forms.Form):
#    user = forms.CharField(max_length = 100)
#    password = forms.CharField(widget = forms.PasswordInput())