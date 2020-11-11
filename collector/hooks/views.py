from django.shortcuts import render
from rest_framework import viewsets
from .serializers import signalsSerializer
from .models import signals
# Create your views here.

class signalsViewSet(viewsets.ModelViewSet):
    queryset = signals.objects.raw("select id, ticker,quote,updated,strategy from hooks_signals where id in (select id from (select ticker,max(id) as id from hooks_signals group by ticker))")
    serializer_class = signalsSerializer