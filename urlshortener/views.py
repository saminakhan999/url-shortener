from django.shortcuts import render, redirect
from .models import Url
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import RequestContext
import string
import random


# Create your views here.

def index(request):
  return render(request, 'urlshortener/index.html')



def redirect_user(request, short_url):
  try:
    shorturl = Url.objects.get(shorturl=short_url)
    print(shorturl)
    return redirect(shorturl.fullurl)
  except:
    return HttpResponseRedirect(reverse("index"))
  



def shorturl_gen():
  shorturl = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(5))
  shorturlexists = Url.objects.filter(shorturl=shorturl)
  if len(shorturlexists) == 0:
    return shorturl
  else:
    return shorturl_gen()

def results(request, shorturl):
  return render(request, 'urlshortener/results.html', {"shorturl":shorturl})

def shortenurl(request):
  if request.method =="POST":
    shorturl = request.POST["shorturl"]
    if len(shorturl) == 0:
      shorturl = shorturl_gen()
    fullurl = request.POST["fullurl"]
    newurl = Url(shorturl = shorturl, fullurl = fullurl)
    try:
      newurl.save()
      return HttpResponseRedirect(reverse("results", args = [shorturl]))
    except:
      return HttpResponseRedirect(reverse("invalidshorturl", args = [shorturl]))


def invalidshorturl(request, shorturl):
  return render(request, 'urlshortener/500.html', {"shorturl":shorturl})


