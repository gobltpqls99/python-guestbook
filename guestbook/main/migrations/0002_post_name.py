# Generated by Django 3.2.4 on 2021-06-07 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
