# Generated by Django 3.2.8 on 2021-10-29 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_alter_blog_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='demo_link',
        ),
    ]
