# Generated by Django 4.0.4 on 2022-07-05 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_recording_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='EmailVerified',
            field=models.BooleanField(default=False),
        ),
    ]