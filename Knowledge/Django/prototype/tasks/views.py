from django import forms
from django import HttpResponseRedirect
from django.shortcuts import render
from django import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tsaks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })
    # Add a new task:
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    else:
        return render(request, "tasks/add.html", {
            "form": NewTaskForm()
        })