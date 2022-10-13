import datetime
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from todolist.models import Task
from todolist.forms import TaskForm


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    list_task = Task.objects.filter(user=request.user)
    context = {
        'user': request.user,
        'list_task': list_task,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))  # membuat response
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='/todolist/login/')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    context = {'form': form}
    return render(request, 'createtask.html', context)


@login_required(login_url='/todolist/login/')
def show_json_todo(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@login_required(login_url='/todolist/login/')
def create_task_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        task = Task.objects.create(user=request.user, date=datetime.date.today(), title=title, description=description)
        data = {
                "pk": task.pk,
                "fields": {
                    "user": task.user,
                    "date": task.date,
                    "title": task.title,
                    "description": task.description,
                }}
        return JsonResponse(data)
    return HttpResponseBadRequest()
