# Generated by Django 4.0.4 on 2022-06-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_CaosNew', '0005_alter_noticia_subtitulo_alter_noticia_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(default='Falta_imagen.jpg', null=True, upload_to='fotos'),
        ),
    ]
