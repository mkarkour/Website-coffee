from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone

class User (models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=128)
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('X','X'),
        )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    admin = models.BooleanField(default = False)
    def __str__(self):
        return self.firstname +' '+ self.lastname

class Livre (models.Model):
    titre = models.CharField(max_length=300)
    auteur = models.CharField(max_length=20)
    id_livre = models.IntegerField(blank=True)
    CATEGORIE_CHOICES = (('S','Scientifique'),
        ('D','Divertissement'),
        ('E','Education'),
        ('L','Littérature'),
        )
    categorie = models.CharField (max_length=1, choices=CATEGORIE_CHOICES, null=True)
    genre = models.CharField (max_length=100, null=True, blank=True)
    def __str__(self):
        return self.titre +' '+ self.auteur



# class Block (models.Model):
#     blockeur = models.ForeignKey("User")
#     blocked = models.ForeignKey("User",related_name = "blocked") 
#     def __str__(self):
#         return self.blockeur.firstname + " bloqué " + self.blocked.firstname 