# Generated by Django 4.0.4 on 2022-06-15 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_CaosNew', '0003_noticia_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='historia',
            field=models.CharField(default='--', max_length=10000),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='subtitulo',
            field=models.CharField(default='--', max_length=200),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(default='--', max_length=200, primary_key=True, serialize=False),
        ),
    ]
