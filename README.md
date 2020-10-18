# Django Rest Framework
O Django Rest Framework (DRF)é uma biblioteca para o Framework Django que disponibiliza funcionalidades para implementar APIs Rest de forma extremamente rápida.

#### Models
Os models são construídos usando a mesma forma dos models para aplicações Django comuns.

#### Views
**Exemplo de View Usando Views Genéricas do DRF**
A class ListCreateAPIView implementa os verbos GET e POST.
A classe RetrieveUpdateDestroyAPIView implementa os verbos PUT e DELETE.

```console
from rest_framework import generics
from livros.models import LivroModel
from livros.serializers import LivroSerializer

class LivroListCreate(generics.ListCreateAPIView):
    queryset = LivroModel.objects.all()
    serializer_class = LivroSerializer

class LivroDetailUpdateAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = LivroModel.objects.all()
    serializer_class = LivroSerializer
```

**Exemplo de view usando a classe viewsets**
A classe ModelViewSet já implementa os verbos GET POST DELETE PUT.

```console
from rest_framework import viewsets
from livros.models import LivroModel
from livros.serializers import LivroSerializer

class TodoList(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
```

#### URLS
Com exceção do uso das views usando as viewsets, as urls são as mesmas do Django padrão, para FBV e CBV.

**Exemplos de urls para viewsets**

```console
from rest_framework.routers import DefaultRouter
from api.views import TodoList

route = DefaultRouter()
route.register(r'', TodoList)
urlpatterns = route.urls
```