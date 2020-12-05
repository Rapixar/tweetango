import random
from django.shortcuts import render
from django.http import JsonResponse, Http404
from .models import Tweet


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    '''
    THIS CLASS TAKES A REQUEST AND RETURNS DATA
    DATA: JSON
    TYPE: REST API VIEW
    CONSUMER: JAVASCRIPT (can be consumed by another client)
    '''
    qs = Tweet.objects.all()
    tweet_list = [{"id": x.id, "content": x.content,
                   "likes": random.randint(0, 500)} for x in qs]
    data = {
        "isUser": False,
        "response": tweet_list,
    }

    return JsonResponse(data)


def tweet_func(response, tweet_id, *args, **kwargs):
    '''
    THIS CLASS TAKES A REQUEST AND RETURNS DATA
    DATA: JSON
    TYPE: REST API VIEW
    CONSUMER: JAVASCRIPT (can be consumed by another client)
    '''
    data = {
        "isUser": False,
        "id": tweet_id,
    }

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
        status = 200
        print(obj)
    except:
        data["message"] = "Not Found"
        status = 404

    '''data = {
        "id": tweet_id,
        "content": obj.content,
        # "image_path": obj.image.url ,
    }'''

    return JsonResponse(data, status=status)


# Create your views here.
