# Generated by Django 4.0.4 on 2022-07-29 11:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_added_pg_trgm'),
    ]

    operations = [
        migrations.AddField(
            model_name='composer',
            name='Alive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='composer',
            name='Birthday',
            field=models.DateField(default=datetime.date(1900, 1, 1)),
        ),
        migrations.AddField(
            model_name='composer',
            name='Country',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='composer',
            name='Deathday',
            field=models.DateField(default=datetime.date(1900, 1, 1)),
        ),
        migrations.AlterField(
            model_name='recording',
            name='Composer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Recordings', to='App.composer'),
        ),
    ]
