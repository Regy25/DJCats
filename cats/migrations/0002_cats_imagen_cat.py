# Generated by Django 3.2.4 on 2021-06-21 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cats',
            name='imagen_cat',
            field=models.ImageField(null=True, upload_to='cats'),
        ),
    ]
