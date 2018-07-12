# Generated by Django 2.0.7 on 2018-07-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(max_length=255, verbose_name="lien de l'image"),
        ),
        migrations.AlterField(
            model_name='product',
            name='url_off',
            field=models.URLField(max_length=255, verbose_name='lien openfoodfacts'),
        ),
    ]
