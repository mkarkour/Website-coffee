# Generated by Django 3.2.4 on 2021-06-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210621_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='titre',
            field=models.CharField(max_length=300),
        ),
    ]
