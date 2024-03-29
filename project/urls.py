"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import todo_list, create_todo,delete_todo, mark_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , todo_list),
    path('create' , create_todo),
    path('<int:pk>/delete' , delete_todo, name='todo_delete'),
    path('<int:pk>/done' , mark_todo, name='todo_done'),

]
