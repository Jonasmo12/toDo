from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


@login_required(login_url='accounts:login')
def index(request):
    user = request.user
    tasks = user.task_set.order_by("-id")
    totalTasks = tasks.count()

    getCompleteTasks = tasks.filter(complete='True')
    getNumberOfCompletedTasks = tasks.filter(complete='True').count()

    noOfInCompleteTasks = tasks.filter(complete='False').count()
    activeTasks = tasks.filter(complete='False')

    # completionRation = totalTasks / getCompleteTasks
    print(totalTasks)

    if request.method == 'POST':

        title = request.POST.get('title')
        task = Task.objects.create(
            title=title,
            user=user,
            complete=False,
        )
        task.save()
        return redirect('/')

    context = {
        'tasks': tasks,
        'getCompleteTasks': getCompleteTasks,
        'getNumberOfCompletedTasks': getNumberOfCompletedTasks,
        'noOfInCompleteTasks': noOfInCompleteTasks,
        'activeTasks': activeTasks,
        'totalTasks': totalTasks,
    }
    return render(request, 'tasks/list.html', context)


@login_required(login_url='accounts:login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'tasks/update_task.html', context)


@login_required(login_url='accounts:login')
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)
