# Generated by Django 4.2.3 on 2023-07-19 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fname',
            field=models.CharField(default='hello', max_length=50),
            preserve_default=False,
        ),
    ]
