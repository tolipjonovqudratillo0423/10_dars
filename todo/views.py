from django.shortcuts import render , redirect
from .models import Todo

def main_page(request):
    todos = Todo.objects.all()
    data = {
        "todos":todos
    }
    return render(request,'index.html',data)

def delete_todo(request, id):
    Todo.objects.filter(id=id).delete()
    return redirect('/') 
def add_todo(request,):
    if request.POST :
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        status = request.POST.get('status')
        Todo.objects.create(
            title=title,
            desc=desc,
            status=status
        )
        return redirect('/')
def update_todo(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == "POST":
        todo.title = request.POST.get("title")
        todo.desc = request.POST.get("desc")
        todo.status = request.POST.get("status")
        todo.save()
        return redirect("/")

    return render(request, "update.html", {"todo": todo})
