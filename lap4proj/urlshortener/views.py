from django.shortcuts import render, redirect
from .models import Url
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import RequestContext

# Create your views here.

def index(request):
  return render(request, 'urlshortener/index.html')



def redirect_user(request, short_url):
  shorturl = Url.objects.get(shorturl=short_url)
  print(shorturl)
  return redirect(shorturl.fullurl)



def shortenurl(request):
  if request.method =="POST":
    shorturl = request.POST["shorturl"]
    fullurl = request.POST["fullurl"]
    newurl = Url(shorturl = shorturl, fullurl = fullurl)
    newurl.save()
    return HttpResponseRedirect(reverse("index"))


def handle500(request):
  response = render('500.html', {}, context_instance=RequestContext(request))
  response.status_code = 500
  return response
