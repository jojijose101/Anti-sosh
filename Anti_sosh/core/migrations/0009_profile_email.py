# Generated by Django 4.1.9 on 2023-06-07 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_profile_firstnm_profile_lastnm'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
