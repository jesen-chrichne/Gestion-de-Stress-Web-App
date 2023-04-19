from django.test import TestCase
from faker import Faker
from .models import User
import random

# Create your tests here.
faker = Faker()

for i in range(10):
    nom_Complet = faker.first_name()
    email = faker.email()
    adresse = faker.country()
    Fonction = faker.job()
    status = random.choice(["Utilisateur Simple","Psychologue"])
    create_user = User(Nom_Complet = nom_Complet,Email = email, Adresse = adresse, Fonction = Fonction, Status = status)
    create_user.save()