# Generated by Django 4.2.8 on 2024-01-15 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-created_date'], 'verbose_name': 'تماس', 'verbose_name_plural': 'تماس ها'},
        ),
    ]