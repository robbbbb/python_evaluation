from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Todo


def index(request):
    return render(request, 'todo.html')


@require_POST
def create_todo(request):
    title = request.POST.get('title')
    if title:
        # this will create todo if title is not empty and a default status False
        todo = Todo.objects.create(title=title, status='False')
        data = {
            'todo': todo.title
        }
        return JsonResponse(data, status=201)
    return JsonResponse({"error_message": "Title is required"}, status=400)


# load todos and search specific todo
def search_todo(request):
    query = request.GET.get("query", "")
    if query:
        todos = Todo.objects.filter(title__icontains=query)
    else:
        todos = Todo.objects.all()

    todo_list = list(todos.values('title'))
    return JsonResponse(todo_list, status=200, safe=False)
