from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import my_todos
from .models import my_entries

def show_todo(request):
    return render(request, "my_todos.html", {"todos": my_todos})

def show_ent(request):
    return render(request,"my_entries.html",{"entry":my_entries})


def get_todo(request, todo_id):
    try:
        return HttpResponse(my_todos[int(todo_id)])
    except IndexError:
        raise Http404("We don't have any.")