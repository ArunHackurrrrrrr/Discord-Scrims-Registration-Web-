# Generated by Django 5.1.3 on 2025-01-19 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration_soft', '0013_userlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='username',
            field=models.CharField(default='not_given', max_length=50),
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='userpass',
            field=models.CharField(default='not_given', max_length=100),
        ),
    ]
