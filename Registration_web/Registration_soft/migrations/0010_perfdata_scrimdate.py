# Generated by Django 5.1.3 on 2025-01-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration_soft', '0009_perfdata_playername1_perfdata_playername2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfdata',
            name='ScrimDate',
            field=models.CharField(default='not found', max_length=20),
        ),
    ]
