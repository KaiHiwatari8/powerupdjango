# Generated by Django 3.0.2 on 2020-01-07 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20200107_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
