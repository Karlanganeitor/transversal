# MIGRO LA IMAGEN 

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='img',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
