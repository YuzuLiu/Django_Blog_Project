# Generated by Django 5.0.4 on 2024-05-02 00:47

import django.db.models.deletion
import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a blog type (e.g. News, food, travel etc.)', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('post_date', models.DateField()),
                ('body', models.TextField(help_text='Enter the content of the blog', max_length=2000)),
                ('blogger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='blog.blogger')),
            ],
        ),
        migrations.AddConstraint(
            model_name='type',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='type_name_case_insensitive_unique', violation_error_message='Type already exists (case insensitive match)'),
        ),
        migrations.AddField(
            model_name='blog',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='blog.type'),
        ),
    ]