# Generated by Django 2.2.2 on 2019-06-30 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allergen', '0008_auto_20190107_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutriment',
            name='image',
        ),
    ]
