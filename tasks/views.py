from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasks
from .forms import TaskForm

# Create your views here.

def index(request):
    tasks = Tasks.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


def update(request, pk):
    task = Tasks.objects.get(id=pk)

    form = TaskForm(instance=task)
    context = {'form': form}
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'tasks/update.html', context)


def delete(request, pk):
    item= Tasks.objects.get(id=pk)
    context = {'item': item}
    if request.method == "POST":
        item.delete()
        return redirect('/')
    return render(request, 'tasks/delete.html', context)
