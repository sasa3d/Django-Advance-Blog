# Generated by Django 3.2.25 on 2025-01-16 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publish_date',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated_at',
            new_name='updated_date',
        ),
    ]
