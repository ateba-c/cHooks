from django.shortcuts import render
from rest_framework import viewsets
from .serializers import signalsSerializer
from .models import signals
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
# Create your views here.

@csrf_exempt 
@require_POST
def tradinghook(request):
    req = json.loads(request.body)
    ticker = req['ticker']
    quote = req['quote']
    tm = req['updated']
    strategy = req['strategy']
    if ticker: # This is where we are verifying the payment
        signal = signals.objects.create(ticker=ticker,quote=quote, updated=tm,strategy=strategy)
        signal.save()
        print(signal)
    return HttpResponse('success')

class signalsViewSet(viewsets.ModelViewSet):
    #queryset = signals.objects.raw("select id, ticker,quote,updated,strategy from hooks_signals where id in (select id from (select ticker,max(id) as id from hooks_signals group by ticker))")
    #obj1=queryset[0]
    #obj2=queryset[1]
    queryset = signals.objects.all()
    serializer_class = signalsSerializer





