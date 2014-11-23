from django.shortcuts import render

from discuss.models import *

def view(request, discussionId):
    discussion = Discussion.objects.get(id = discussionId)
    discussion.viewCount += 1
    discussion.save()

    return render(request, "discuss/discussions/view.html", {
        "discussion": discussion
    })
