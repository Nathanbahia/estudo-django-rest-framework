from rest_framework import generics

from livros.models import LivroModel
from livros.serializers import LivroSerializer


class LivroListCreate(generics.ListCreateAPIView):
    queryset = LivroModel.objects.all()
    serializer_class = LivroSerializer


class LivroDetailUpdateAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = LivroModel.objects.all()
    serializer_class = LivroSerializer
