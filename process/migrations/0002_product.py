# Generated by Django 5.0.2 on 2024-02-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=255, null=True)),
                ('formula', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
