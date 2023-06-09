# Generated by Django 4.1.7 on 2023-02-28 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0003_alter_categorie_cat_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='cat_name',
            field=models.CharField(choices=[('Al', 'Alimentaire'), ('Mb', 'Meuble'), ('Sn', 'Sanitaire'), ('Vs', 'Vaisselle'), ('Vt', 'Vêtement'), ('Jx', 'Jouets'), ('Lg', 'Linge de Maison'), ('Bj', 'Bijoux'), ('Dc', 'Décor')], default='Alimentaire', max_length=50),
        ),
    ]
