from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'books/add/$', views.BookCreate.as_view(), name='book-add'),
    url(r'^delete/(?P<pk>\d+)/$', views.BookDelete.as_view(), name='delete')
]