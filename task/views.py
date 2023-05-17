from django.shortcuts import render, HttpResponse, redirect
from .models import *
from datetime import datetime

# Create your views here.

def index(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        foram = Task(title = title)
        foram.save()
        return redirect('/')
        

    context = {'tasks': tasks}
    return render(request, "index.html", context)

def update(request, pk):
    task = Task.objects.get(id = pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        complete = request.POST.get('complete')

        if complete == 'on': # explaination for this in update.html
            task.complete = True
        else:
            task.complete = False
        task.title = title
        task.save()
        return redirect('/')

    context = {'task': task}
    return render(request, "update.html", context)

def delete(request, pk):
    tasks = Task.objects.get(id = pk)

    if request.method == 'POST':
        tasks.delete()
        return redirect('/')    
    
    context = {'tasks': tasks}
    return render(request, "delete.html", context)
