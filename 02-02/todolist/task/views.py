from django.shortcuts import render,redirect
from . import models

def index(req):
    if req.POST:
        models.Task.objects.create(name=req.POST['name'])
        return redirect('/') 

    tasks = models.Task.objects.all()
    return render(req, 'task/index.html', {
        'data': tasks,
    })

def detail(req, id):
    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Task.objects.filter(pk=id).delete()
    return redirect('/')
