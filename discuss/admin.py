from django.contrib import admin

from .models import *

class SubjectAdmin(admin.ModelAdmin):
    pass

class DiscussionAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class TranscriptionAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class RelatedLinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Transcription, TranscriptionAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(RelatedLink, RelatedLinkAdmin)
