# Generated by Django 4.0.4 on 2022-05-27 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quad_dj_app', '0005_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='user',
        ),
    ]
