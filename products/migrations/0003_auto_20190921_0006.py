# Generated by Django 2.2.5 on 2019-09-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(null=True, upload_to='products/'),
        ),
    ]