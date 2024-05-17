from django.shortcuts import render
from .serializers import MeterSerializers,MeterDetailSerializers, Meter, Meter_Data,MeterDataSerializers
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.views.generic.list import ListView

# Create your views here.

class MeterListView(ListView):
    """
         View to display a list of Meter objects in HTML format.
    """
    
    model = Meter
    template_name = "MeterList.html"
    permission_classes = [AllowAny]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meters = Meter.objects.all()
        serializer = MeterSerializers(meters, many=True)
        context['meters_data'] = serializer.data
        return context
    
class MeterCreateView(generics.CreateAPIView):
    """
    POST: create Meter instance.
    """

    queryset = Meter.objects.all()
    serializer_class = MeterSerializers
    permission_classes = [AllowAny]


class MeterDataCreateView(generics.CreateAPIView):
    """
    GET: Create meter data instances
    """

    queryset = Meter_Data.objects.all()
    serializer_class = MeterDataSerializers
    permission_classes = [AllowAny]

class MeterDetailsView(generics.RetrieveAPIView):
    """
    GET: Retrieve the specific Meter instances along with their associate meter_data
    """

    queryset = Meter.objects.all()
    serializer_class = MeterDetailSerializers
    permission_classes = [AllowAny]