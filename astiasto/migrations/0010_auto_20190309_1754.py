# Generated by Django 2.1.7 on 2019-03-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astiasto', '0009_auto_20180308_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
