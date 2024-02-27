from django.shortcuts import render

from .models import Todo


def todo_list(request):
    data = Todo.objects.all()
    return render(request,'list.html',{'todos':data})


