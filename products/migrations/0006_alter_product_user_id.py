# Generated by Django 5.0.2 on 2024-02-27 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_height_alter_product_image_and_more'),
        ('users', '0007_gender_userprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user_id',
            field=models.ManyToManyField(blank=True, to='users.userprofile'),
        ),
    ]
