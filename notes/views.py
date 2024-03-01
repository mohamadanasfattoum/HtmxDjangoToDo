from django.shortcuts import render

from .models import Todo


def todo_list(request):
    data = Todo.objects.all()
    return render(request,'main.html',{'todos':data})


def create_todo(request):
    note = request.POST['note']
    todo = Todo.objects.create(note=note)

    todos = Todo.objects.all()
    return render(request,'todo_list.html',{'todos':todos})

