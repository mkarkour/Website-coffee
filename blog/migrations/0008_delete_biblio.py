# Generated by Django 3.2.4 on 2021-06-21 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_livre_titre'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Biblio',
        ),
    ]