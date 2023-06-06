from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {
        'tasks': Task.objects.all().order_by('id')
    })

def task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        return render(request, 'tasks/task.html', {
            'task': task
        })
    except Task.DoesNotExist:
        return redirect('/')
            
def new(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task = Task.objects.create(title=title, description=description)
        messages.success(request, 'Create task successfully')
        return redirect('/')
    else:
        return render(request, 'tasks/new.html')


def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    messages.success(request, 'Deleted task successfully!')
    return redirect('/')

def edit(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        if request.method == 'POST':
            task.title = request.POST['title']
            task.description = request.POST['description']
            task.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('/')
        else: 
            return render(request, 'tasks/edit.html', {
                "task": task
            })
    except Task.DoesNotExist:
        return redirect('/')

def error_404_view(request, exception):
    return render(request, 'tasks/404.html')