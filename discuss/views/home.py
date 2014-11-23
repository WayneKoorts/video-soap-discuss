from django.shortcuts import render

from discuss.models import *

def index(request):
    subjects = Subject.objects.all()

    return render(request, "discuss/home.html", {
        "subjects": subjects
    })
