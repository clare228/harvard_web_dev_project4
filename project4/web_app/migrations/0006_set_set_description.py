# Generated by Django 2.0.3 on 2020-05-24 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0005_set_set_colour'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='set_description',
            field=models.CharField(blank=True, default='enter_description', max_length=1000, null=True),
        ),
    ]
