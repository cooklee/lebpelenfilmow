# Generated by Django 4.1 on 2022-08-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]