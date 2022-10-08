from dataclasses import fields
import datetime
from urllib import response
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from todolist.models import TodoListEntry
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='login/')
def show_todolist(request):
    data_todo = TodoListEntry.objects.filter(user=request.user)
    context = {
    'todo': data_todo,
    }
    return render(request, "todolist.html",context=context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='login/')
def show_create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = TodoListEntry.objects.create(title=title, description=description,date=datetime.date.today(), is_finished=False, user=request.user)
        response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
        return response

    return render(request, "create.html")

def update_finished(request,id):

    task = get_object_or_404(TodoListEntry, id = id)
    task.is_finished = not task.is_finished
    task.save()

    return redirect('todolist:show_todolist')

def delete_todo(request,id):

    task = get_object_or_404(TodoListEntry, id = id)
    task.delete()

    return redirect('todolist:show_todolist')

def show_json(request):
    data = TodoListEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = TodoListEntry.objects.create(title=title, description=description,date=datetime.date.today(), is_finished=False, user=request.user)

        result = {
            'fields':{
                'title':todo.title,
                'description':todo.description,
                'is_finished':todo.is_finished,
                'date':todo.date,
            },
            'pk':todo.pk
        }



        return JsonResponse(result)
