from django.shortcuts import render

from .models import Todo


def todo_list(request):
    data = Todo.objects.all()
    return render(request,'main.html',{'todos':data})


def create_todo(requste):
    title = requste.POST['title']
    todo = Todo.objects.create(title=title)

    todos = Todo.objects.all()
    return render(request,'list.html',{'todos':todos})

