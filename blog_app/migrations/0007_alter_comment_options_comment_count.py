# Generated by Django 4.2.8 on 2024-02-03 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_post_tags_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='comment',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
