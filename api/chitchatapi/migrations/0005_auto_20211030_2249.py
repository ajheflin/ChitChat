# Generated by Django 3.2.8 on 2021-10-30 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chitchatapi', '0004_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='modified',
            new_name='last_modified',
        ),
        migrations.AddField(
            model_name='chat',
            name='creator',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.PROTECT, related_name='creator_id', to='chitchatapi.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='recipient',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.PROTECT, related_name='recipient_id', to='chitchatapi.user'),
            preserve_default=False,
        ),
    ]