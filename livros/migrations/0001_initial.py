# Generated by Django 3.1.2 on 2020-10-17 23:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LivroModel',
            fields=[
                ('livro_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('titulo', models.CharField(max_length=255, verbose_name='Livro')),
                ('autor', models.CharField(max_length=255, verbose_name='Autor')),
                ('editora', models.CharField(max_length=255, verbose_name='Editora')),
                ('genero', models.CharField(choices=[['1', 'Administração'], ['2', 'Auto-Ajuda'], ['3', 'Comédia'], ['4', 'Culinária'], ['5', 'Drama'], ['6', 'Romance'], ['7', 'Tecnologia']], max_length=50, verbose_name='Gênero')),
                ('publicacao', models.PositiveIntegerField(verbose_name='Ano de Publicação')),
                ('capa', models.ImageField(upload_to='media')),
                ('criacao', models.DateField(auto_now_add=True, verbose_name='Criação')),
            ],
        ),
    ]
