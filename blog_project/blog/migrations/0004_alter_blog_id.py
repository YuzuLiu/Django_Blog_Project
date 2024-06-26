# Generated by Django 5.0.4 on 2024-05-02 02:53

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogger_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular blog across whole website', primary_key=True, serialize=False),
        ),
    ]
