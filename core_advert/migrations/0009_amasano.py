# Generated by Django 4.1.2 on 2023-01-14 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_advert', '0008_indamukanyo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amasano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.FileField(upload_to='amasano/descriptions')),
            ],
        ),
    ]