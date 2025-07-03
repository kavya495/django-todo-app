from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def index(request):
    tasks=Task.objects.all()
    if request.method=='POST':
        title=request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('/')
    return render(request,'index.html',{'tasks':tasks})
def delete_task(request,task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('/')
def complete_task(request,task_id):
    task=Task.objects.get(id=task_id)
    task.completed=True
    task.save()
    return redirect('/')
def uncomplete_task(request,task_id):
    task=Task.objects.get(id=task_id)
    task.completed=False
    task.save()
    return redirect('/')
def edit_task(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=='POST':
        task.title=request.POST.get('title')
        task.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task})