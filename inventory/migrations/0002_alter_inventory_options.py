# Generated by Django 4.2.4 on 2023-08-08 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'ordering': ('name',), 'verbose_name_plural': 'Inventory'},
        ),
    ]