from django.shortcuts import render, redirect
from .models import TodoItem
# Create your views here.

def home(request):
	all_todo_items = TodoItem.objects.all()
	return render(request, 'todo.html', { 'all_items':all_todo_items}) # all_items be used in for loops



def addTodo(request):
	new_item = TodoItem(content =  request.POST['content'] )
	new_item.save()
	return redirect('home')
	# create new todo all_items
	# save 
	# redirect to  /todo/'


def deleteTodo(request, todo_id):
	item_to_delete = TodoItem.objects.get(id = todo_id)
	item_to_delete.delete()
	return redirect('home')
\