# Generated by Django 2.1.2 on 2018-10-04 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('restricao_etaria', models.IntegerField(choices=[('LIVRE', 0), ('INFANT', 3), ('CHILD', 5), ('YOUNG', 10), ('TEEN', 13), ('ADULT', 16), ('FORIBEN', 18)], verbose_name='Restrição de Idade')),
                ('data_publicacao', models.DateField(auto_now_add=True)),
                ('completa', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autor.Autor', verbose_name='autor')),
                ('categorias', models.ManyToManyField(to='categoria.Categoria', verbose_name='categorias')),
                ('generos', models.ManyToManyField(to='historia.Genero', verbose_name='')),
            ],
        ),
    ]
