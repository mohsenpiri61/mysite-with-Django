# Generated by Django 4.2.8 on 2024-02-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_remove_comment_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='login_needed',
            field=models.BooleanField(default=False),
        ),
    ]