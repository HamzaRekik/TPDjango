from django.db import models

# Create your models here.
class Categorie(models.Model):
    Cat_CHOICES=[('Alimentaire','Alimentaire'),('Meuble','Meuble'),
    ('Sanitaire','Sanitaire'), ('Vaisselle','Vaisselle'),
    ('Vêtement','Vêtement'),('Jouets','Jouets'),
    ('Linge de Maison','Linge de Maison'),('Bijoux','Bijoux'),('Décor','Décor')]
    cat_name = models.CharField(max_length=50 , choices=Cat_CHOICES , default='Alimentaire')

    def __str__(self):
        return self.cat_name

class Fournisseur(models.Model):
    nom = models.CharField(max_length=50 ,null=True)
    adresse = models.TextField()
    email = models.EmailField(max_length=40 , null=True)
    telephone = models.CharField(max_length=8 , null=True)

    def __str__(self):
        return self.nom



class Produit(models.Model):
    TYPE_CHOICES=[
    ('em','emballe'),
    ('fr','Frais'),
    ('cs','Conserve')]
    libelle = models.CharField(max_length=100)
    description = models.TextField(default='Non définie')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE , null=True)
    Fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE , null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=3 , default=0.000)
    type = models.CharField(max_length=2 , choices=TYPE_CHOICES , default='em')
    image = models.ImageField(upload_to='media/', blank=True )
    

    def __str__(self):
        return self.libelle

