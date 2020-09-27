from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import TodoForm
from .models import Todo
# Create your views here.
def home_view(requests):
	#return HttpResponse("The TODO app")
	form=TodoForm(requests.POST or None) #To add todo list
	if form.is_valid():
		form.save()
		form=TodoForm()

	obj=Todo.objects.all() #To render todo list

	context={
	'context_form':form,
	"context_obj":obj
	}
	return render(requests, "home.html", context)


def delete_view(requests, todo_id):
	obj=Todo.objects.get(id=todo_id)
	if requests.method=="POST":
		obj.delete()
		return HttpResponseRedirect("/")
	context={'context_obj':obj}
	return render(requests, "delete.html", context)

# def delete_list_view(requests):
# 	obj=Todo.objects.all()
# 	context={
# 	"context_obj":obj
# 	}
# 	return render(requests, "delete_list_view.html", context)