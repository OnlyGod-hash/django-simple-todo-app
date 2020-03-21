from django.urls import path
from .views import home,addTodo,deleteTodo

urlpatterns = [
    path('', home, name ="home"),
    path('addTodo/', addTodo, name ="addTodo"),
    path('deleteTodo/<int:todo_id>/', deleteTodo, name ="deleteTodo"),
   

]
