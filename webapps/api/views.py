import os
import random, string
from urllib.parse import unquote, urljoin
from django.http import HttpResponse
from django.shortcuts import redirect
from . import redis

# Create your views here.

def randomname(n):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

async def get_shorturl(request):

    url = unquote(request.GET.get('url'))

    for _ in range(10):
        key = await register(url)
        if key:
            return HttpResponse(urljoin(os.environ['ROOT_URL'], key))

    return HttpResponse(status=503)

async def register(url):
    key = randomname(10)
    ok = await redis.set(key, url, expire=5184000, exist=redis.SET_IF_NOT_EXIST)
    if ok:
        return key

    return None

async def get_url(request, key):

    url = await redis.get(key)

    if url:
        return redirect(url)

    return HttpResponse(status=404)