from django.shortcuts import render, redirect
from mongoengine.queryset.visitor import Q
from .models import Task
from django.utils import timezone
from bson import ObjectId

# Create your views here.

def index(request):
    return render(request, 'index.html')

def task_list(request):
    tasks = list(Task.objects.all())
    for task in tasks:
        task.task_id = str(task._id)
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        task = Task(
            title = request.POST['title'],
            description = request.POST['description']
        )
        try:
            task.save()
            return redirect(task_list)
        except Exception as e:
            print(f"Error during task.save(): {e}")
    return render(request, 'add_task.html')

def complete_task(request):
    task_id = request.GET.get('task_id')
    print(f"task_id: {task_id}")
    task = Task.objects(_id=ObjectId(task_id)).first()
    if task:
        task.completed = True
        task.completed_at = timezone.now()
        task.save()
    return redirect(task_list)

def delete_task(request):
    task_id = request.GET['task_id']
    task = Task.objects(_id=ObjectId(task_id)).first()
    task.delete()
    return redirect(task_list)