# Generated by Django 4.2.2 on 2023-06-24 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='datetime',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='supplier',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
