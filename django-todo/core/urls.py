"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from todo.views import complete_todo, get_todo_list, get_completed_todo_list, get_progress_todo_list, init_db
from todo.views import TodoDetailView, TodoCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_todo_list, name="todo_list"),
    path('completed/', get_completed_todo_list, name="completed_todo_list"),
    path('progress/', get_progress_todo_list, name="progress_todo_list"),
    path('create/', TodoCreateView.as_view(), name="create_todo"),
    path('<int:todo_id>/', TodoDetailView.as_view(), name="todo_detail"),
    path('<int:todo_id>/complete/', complete_todo, name="todo_complete"),
    path('init/', init_db),
]
