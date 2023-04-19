from django.shortcuts import render
from django.http import HttpResponse
from .models import  Todo
# Create your views here.

tasks = {"task_1": "Убери комнату","task_2": "Купи продукты"}

def main_page(request):
	todos = Todo.objects.all()
	print(todos)
	return render(request,"todo/index.html", {'todos': todos})
	
def about_page(request):
	return HttpResponse("Привет Привет")
