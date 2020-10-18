from django.db import models
from uuid import uuid4


def upload_livro(instance, filename):
    return f"{instance.livro_id}-{filename}"


GENEROS = (    
    ['Administração', 'Administração'],
    ['Auto-Ajuda', 'Auto-Ajuda'],
    ['Comédia', 'Comédia'],
    ['Culinária', 'Culinária'],
    ['Drama', 'Drama'],
    ['Romance', 'Romance'],            
    ['Tecnologia', 'Tecnologia'],
)


class LivroModel(models.Model):
    livro_id = models.UUIDField('Id', default=uuid4 ,primary_key=True, editable=False)
    titulo = models.CharField('Livro', max_length=255)
    autor = models.CharField('Autor', max_length=255)
    editora = models.CharField('Editora', max_length=255)
    genero = models.CharField('Gênero', choices=GENEROS, max_length=50)
    publicacao = models.PositiveIntegerField('Ano de Publicação')
    capa = models.ImageField(upload_to=upload_livro)
    criacao = models.DateField('Criação', auto_now_add=True)

    def __str__(self):
        return self.titulo
