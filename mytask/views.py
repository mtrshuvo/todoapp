from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from . import models
from .forms import * 

# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mytask:task')

    context = {'tasks':tasks, 'form':form}

    return render(request,'mytask/list.html',context)

def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method=="POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('mytask:task')
    context = {'form':form}   
    return render(request,'mytask/update_task.html',context)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    context = {'item':item}
    if request.method=="POST":
        item.delete()
        return redirect('mytask:task')

    return render(request,'mytask/delete.html',context)

