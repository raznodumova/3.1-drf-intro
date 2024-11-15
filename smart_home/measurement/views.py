# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import generics
from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer


class ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class RetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class CreateAPIView(generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class ListSensors(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer