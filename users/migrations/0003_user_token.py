# Generated by Django 4.2.2 on 2024-04-20 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_country_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Token'),
        ),
    ]
