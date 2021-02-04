from django.shortcuts import render, get_object_or_404, reverse, redirect

from todo.forms import TaskForm
# Create your views here.
from todo.models import Task


def list_view(request):
    task_list = Task.objects.all()

    return render(request, 'todo/index.html', {'task_list': task_list})


def detail_view(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    return render(request, 'todo/detail.html', {'task_obj': task_obj})


def add(request):
    form = TaskForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            obj = form.save()
            return redirect(reverse('todo:detail', kwargs={'pk': obj.pk}))
        else:
            return render(request, 'todo/task_form.html', {'form': form, 'type': 'add'})

    return render(request, 'todo/task_form.html', {'form': form, 'type': 'ADD'})


def edit(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('todo:detail', kwargs={'pk': pk}))
    return render(request, 'todo/task_form.html', {'form': form, 'type': 'UPDATE'})


def delete(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    obj.delete()
    return redirect(reverse('todo:index'))
