import os
import random, string
from urllib.parse import unquote, urljoin, urlparse
from django.http import HttpResponse
from django.shortcuts import redirect
from . import redis

# Create your views here.

def get_key(n):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

async def get_shorturl(request):

    url = unquote(request.GET.get('url'))

    o = urlparse(url)
    if len(o.scheme) == 0 or len(o.netloc) == 0:
        return HttpResponse(status=400)

    root = os.environ['ROOT_URL']

    for _ in range(10):
        key = await register(url)
        if key:
            return HttpResponse(urljoin(root, key))

    return HttpResponse(status=503)

async def register(url):
    
    strlen = int(os.environ['STR_LENGTH'])
    key = get_key(strlen)
    expire = int(os.environ['EXPIRE'])

    ok = await redis.set(key, url, expire=expire, exist=redis.SET_IF_NOT_EXIST)
    if ok:
        return key

    return None

async def get_url(request, key):

    url = await redis.get(key)

    if url:
        return redirect(url)

    return HttpResponse(status=404)