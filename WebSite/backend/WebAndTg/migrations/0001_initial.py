# Generated by Django 5.1.2 on 2024-10-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=40)),
                ('product', models.CharField(max_length=40)),
                ('Description', models.TextField()),
                ('Photo', models.TextField()),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
