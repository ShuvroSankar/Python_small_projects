from django.shortcuts import render, redirect
from .models import Task
from django.shortcuts import get_object_or_404
from .forms import TodoForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = "myapp/index.html"
    context_object_name = "task_list"


class TaskDetailView(DetailView):
    model = Task
    template_name = "myapp/detail.html"
    context_object_name = "task"


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "myapp/update.html"
    context_object_name = "task"
    fields = ["name", "priority", "date"]

    def get_success_url(self):
        return reverse_lazy("cbvdetail", kwargs={"pk": self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "myapp/delete.html"
    success_url = reverse_lazy("cbvindex")


def index(request):
    task_list = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get("name", "")
        priority = request.POST.get("priority", "")
        date = request.POST.get("date", "")
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect("/")
    return render(request, "myapp/index.html", {"task_list": task_list})


def delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect("/")
    return render(request, "myapp/delete.html", {"task": task})


def update(request, id):
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "myapp/edit.html", {"form": form, "task": task})
