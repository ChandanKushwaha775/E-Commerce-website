# Generated by Django 3.0.5 on 2020-11-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blogpost_head2'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='head2',
            field=models.CharField(default='', max_length=500),
        ),
    ]