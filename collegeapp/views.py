from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.urls import reverse

# Create your views here.
def applied_list(request):
    student_apply= "Student Apply"
    student_register = "Student Register"
    student_login = "Student Login"
    context = {"student_apply":student_apply, "student_register":student_register, "student_login":student_login}
    return render(request, 'collegeapp/applied_list.html', context)

def apply_link(request):
    if request.method == 'POST':
        Apply.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            marks=request.POST['marks'],
            intermediate=request.POST['intermediate']
        )

        return HttpResponseRedirect(reverse('collegeapp:applied_list'))
    return render(request, 'collegeapp/apply_link.html')

def eligible(request):
    if request.method == 'POST':
        Register.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password'],
            department=request.POST['department'],
            fname=request.POST['fname'],
            nationality=request.POST['nationality']
        )
        return HttpResponseRedirect(reverse('collegeapp:applied_list'))
    return render(request, 'collegeapp/eligible.html')

def login(request):
    if request.method == 'POST':
        Register.objects.create(
            email = request.POST['email'],
            password = request.POST['password']
        )
        return render(request, 'collegeapp/eligible.html')

