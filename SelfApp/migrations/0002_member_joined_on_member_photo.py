# Generated by Django 5.1.6 on 2025-04-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SelfApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joined_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='member',
            name='photo',
            field=models.ImageField(default='a.png', upload_to='uploads/'),
        ),
    ]
