# Generated by Django 4.1.3 on 2024-03-09 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='is_featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]