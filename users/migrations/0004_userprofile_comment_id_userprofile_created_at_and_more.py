# Generated by Django 5.0.2 on 2024-02-24 02:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_content_alter_comment_post_id_and_more'),
        ('events', '0001_initial'),
        ('users', '0003_alter_userprofile_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='comment_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.comment'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='event_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.event'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
