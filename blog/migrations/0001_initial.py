# Generated by Django 3.2.4 on 2021-06-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=128)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('X', 'X')], max_length=1)),
                ('acheteur', models.BooleanField(default=False)),
                ('vendeur', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
    ]
