from django.shortcuts import render
from rest_framework.response import Response

from events.models import Eventer
from .serializers import EventerSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def eventList(request):
    events = Eventer.objects.all()
    serializer= EventerSerializer(events, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def eventDetails(request, pk):
    events = Eventer.objects.get(id=pk)
    serializer = EventerSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def eventCreate(request):
    serializer = EventerSerializer(data= request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def eventUpdate(request, pk):
    event = Eventer.objects.get(id=pk)
    serializer = EventerSerializer(instance=event, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['Delete'])
def eventDelete(request, pk):
    event = Eventer.objects.get(id=pk)
    event.delete()

    return Response('Deleted')






