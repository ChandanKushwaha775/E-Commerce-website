# Generated by Django 3.0.5 on 2020-11-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201110_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=200)),
                ('mobile_number', models.IntegerField(max_length=40)),
                ('landmark', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=2000)),
                ('address_line2', models.CharField(max_length=2000)),
                ('state', models.CharField(max_length=90)),
                ('city', models.CharField(max_length=90)),
                ('zip_code', models.IntegerField(max_length=20)),
            ],
        ),
    ]