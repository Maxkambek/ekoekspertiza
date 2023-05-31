from rest_framework import generics
from .serializers import FunctionsSerializer, AnswerSerializer, XizmatlarSerializer
from .models import Functions, AnswerQuestions, Xizmatlar


class FunctionAPIView(generics.ListAPIView):
    queryset = Functions.objects.all()
    serializer_class = FunctionsSerializer


class AnswerAPIView(generics.ListAPIView):
    queryset = AnswerQuestions.objects.all()
    serializer_class = AnswerSerializer


class XizmatlarAPIView(generics.ListAPIView):
    queryset = Xizmatlar.objects.all()
    serializer_class = XizmatlarSerializer
