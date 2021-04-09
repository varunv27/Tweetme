from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
# Create your views here.
from .models import Tweet

def tweet_list_view(request, *args, **kwargs):
    '''
    REST API VIEW
    Consume by Javascript
    return json data
    '''
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    '''
    REST API VIEW
    Consume by Javascript
    return json data
    '''
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404
    
    return JsonResponse(data, status=status) 

    #return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content}</h1>")


def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)
