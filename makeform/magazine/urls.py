from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'magazine.views.index', name="index"),
    url(r'^new/$', 'magazine.views.new', name="new"),
    url(r'^(?P<pk>\d+)/$', 'magazine.views.detail', name="detail"),
    url(r'^(?P<pk>\d+)/comment/new/$', 'magazine.views.comment_new', name="comment_new"),
    url(r'^(?P<pk>\d+)/edit/$', 'magazine.views.edit', name="edit"),
    url(r'^(?P<pk>\d+)/delete/$', 'magazine.views.delete', name="delete"),
]
