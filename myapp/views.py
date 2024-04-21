from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    #return HttpResponse("Hello WOrld")
    return render(request, "home.html")

def todos(request):

    # Retrieved all the ToDoItems from the database
    items = TodoItem.objects.all()
    return render(request, "todos.html", { "todos": items})