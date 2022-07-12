from django.shortcuts import render
from random import randint

def nippoListView(request):
    return render(request, "nippo/nippo_list.html")

def nippoDetailView(request,number):
    template_name = "nippo/nippo_detail.html"
    random_int = randint(1,10)
    ctx = {
        "random_number": random_int,
        "number": number,
    }
    return render(request, template_name, ctx)

def nippoCreateView(request):
    template_name = "nippo/nippo_form.html"

    if request.POST:
        title = request.POST["title"]
        content = request.POST["content"]

    return render(request, template_name)
# Create your views here.
