# Generated by Django 3.2.4 on 2021-06-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cat', models.CharField(max_length=30)),
                ('ascii_cat', models.TextField()),
                ('desc_cat', models.CharField(max_length=200)),
                ('imagen_cat', models.ImageField(null=True, upload_to='cats')),
            ],
        ),
    ]
