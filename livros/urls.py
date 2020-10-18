from django.urls import path
from livros.views import LivroListCreate, LivroDetailUpdateAndDelete


urlpatterns = [
    path('', LivroListCreate.as_view()),
    path('<str:pk>', LivroDetailUpdateAndDelete.as_view())
]
