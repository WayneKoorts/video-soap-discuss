from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns("",
    url(r"^$", "discuss.views.home.index", name = "index"),

    # Subjects.
    url(r"^subjects/$", "discuss.views.subjects.index", name = "subjectIndex"),
    url(r"^subjects/view/(\d+)/$", "discuss.views.subjects.view", name = "viewSubject"),

    # Admin.
    url(r"^admin/", include(admin.site.urls)),
)
