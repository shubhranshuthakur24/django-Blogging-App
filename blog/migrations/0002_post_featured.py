# Generated by Django 2.2 on 2020-03-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='FEATURED',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
