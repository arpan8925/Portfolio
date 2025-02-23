# Generated by Django 5.1.6 on 2025-02-22 17:36

import ckeditor.fields
import django.utils.timezone
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_project_banner_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='similar_description',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
