# Generated by Django 4.2.7 on 2024-03-17 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercredentials', '0002_alter_profile_firstname_alter_profile_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilePicture',
            field=models.ImageField(blank=True, upload_to='profile'),
        ),
    ]
