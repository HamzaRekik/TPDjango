# Generated by Django 4.2.1 on 2023-05-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0008_rename_image_produit_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]