# Generated by Django 2.0.4 on 2018-05-29 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20180529_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='isactived',
            field=models.BooleanField(default=True, verbose_name='是否有效'),
        ),
    ]
