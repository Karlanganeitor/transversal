# Generated by Django 3.1.2 on 2021-07-22 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_producto_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img',
            field=models.ImageField(default=1, upload_to='productos'),
            preserve_default=False,
        ),
    ]