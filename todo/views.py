from django.shortcuts import render
from .models import Todo

def main_page(request):
    todos = Todo.objects.all()
    data = {
        "todos":todos
    }
    return render(request,'index.html',data)