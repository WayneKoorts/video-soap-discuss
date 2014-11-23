from django.shortcuts import render, redirect

from discuss.models import *

def index(request):
    return render(request, "discuss/subjects/index.html", {
        "subjects": Subject.objects.all()
    })

def view(request, subjectId):
    subject = Subject.objects.get(id = subjectId)

    return render(request, "discuss/subjects/view.html", {
        "subject": subject,
        "discussions": subject.discussions.all()
    })
