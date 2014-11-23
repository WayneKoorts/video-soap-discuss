from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    creator = models.ForeignKey(User)
    createdTimestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Discussion(models.Model):
    title = models.CharField(max_length = 300, unique = True)
    creator = models.ForeignKey(User)
    createdTimestamp = models.DateTimeField(auto_now_add = True)
    viewCount = models.PositiveIntegerField(blank = True, default = 0)
    subject = models.ForeignKey("Subject", related_name = "discussions")
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.title

class Post(models.Model):
    VIDEO = 0
    AUDIO = 1
    TEXT = 2

    postTypeChoices = (
        (VIDEO, "Video"),
        (AUDIO, "Audio"),
        (TEXT, "Text")
    )

    user = models.ForeignKey(User)
    discussion = models.ForeignKey("Discussion", related_name = "posts")
    createdTimestamp = models.DateTimeField(blank = True, auto_now_add = True)
    modifiedTimestamp = models.DateTimeField(blank = True, auto_now = True)
    postType = models.PositiveIntegerField(blank = True, choices = postTypeChoices)

    # The following fields are mutually exclusive. Which one is filled
    # depends on the postType value.
    mediaUrl = models.URLField(blank = True, null = True) # Applies to audio and video.
    text = models.TextField(blank = True, null = True)

    def __str__(self):
        return str.format("{0} in {1}", self.user.username, self.discussion.title)

class Transcription(models.Model):
    text = models.TextField()
    lastEditedBy = models.ForeignKey(User)
    post = models.OneToOneField("Post", blank = True)

    def __str__(self):
        return self.videoPost.dicussion.title if self.self.videoPost else self.audioPost.discussion.title

class Tag(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.name

class RelatedLink(models.Model):
    url = models.URLField()
    post = models.ForeignKey("Post")
