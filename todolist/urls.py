from django.urls import path
from todolist.views import add_todo, delete_task, delete_todo,show_json, show_todolist, register,login_user,logout_user, show_create_todo, update_finished, delete_todo

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name="show_todolist"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('create-task/', show_create_todo, name='show_create_todo'),
    path('add/', add_todo, name='add_todo'),
    path('json/', show_json, name='show_json'),
    path('<id>/update/', update_finished, name='update'),
    path('<id>/delete/', delete_todo, name='delete'),
    path('delete/<id>/', delete_task, name='delete_task'),


]