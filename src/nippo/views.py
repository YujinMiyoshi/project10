from django.shortcuts import render
from random import randint
from .models import NippoModel

def nippoListView(request):
    ctx={}
    qs = NippoModel.objects.all()
    ctx["object_list"] = qs
    return render(request, "nippo/nippo_list.html", ctx)

def nippoDetailView(request, pk):
    template_name = "nippo/nippo_detail.html"
    random_int = randint(1,10)
    q = NippoModel.objects.get(pk = pk)
    ctx = {
        "random_number": random_int,
        "number": pk,
        "object":q,
    }
    return render(request, template_name, ctx)

def nippoCreateView(request):
    template_name = "nippo/nippo_form.html"

    if request.POST:
        title = request.POST["title"]
        content = request.POST["content"]
        obj = NippoModel(title=title, content=content)
        obj.save()

    return render(request, template_name)
# Create your views here.
