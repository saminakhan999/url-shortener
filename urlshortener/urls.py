from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name='index'),
  path("results/<str:shorturl>", views.results, name='results'),
  path("<str:short_url>", views.redirect_user, name='redirect_user'),
  path("create/", views.shortenurl, name='shortenurl'),
  path("invalidshorturl/<str:shorturl>", views.invalidshorturl, name='invalidshorturl')

]
