# Generated by Django 4.1.7 on 2023-03-14 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0006_fournisseur_produit_fournisseur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
