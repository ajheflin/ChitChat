# Generated by Django 3.2.8 on 2021-10-30 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chitchatapi', '0007_auto_20211030_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='chats',
            field=models.ManyToManyField(blank=True, null=True, to='chitchatapi.Chat'),
        ),
    ]
