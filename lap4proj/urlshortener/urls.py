from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name='index'),
  path("<str:short_url>", views.redirect_user, name='redirect_user'),
  path("create/", views.shortenurl, name='shortenurl')
]
