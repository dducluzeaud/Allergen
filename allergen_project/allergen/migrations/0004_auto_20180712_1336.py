# Generated by Django 2.0.7 on 2018-07-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergen', '0003_auto_20180711_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrimentcomposeproduct',
            name='nutriment_quantity',
            field=models.DecimalField(decimal_places=6, max_digits=12),
        ),
        migrations.AlterField(
            model_name='vitamincomposeproduct',
            name='vitamin_quantity',
            field=models.DecimalField(decimal_places=6, max_digits=12),
        ),
    ]
