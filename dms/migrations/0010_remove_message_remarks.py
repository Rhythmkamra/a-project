# Generated by Django 4.2.2 on 2024-03-17 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0009_alter_message_message_alter_message_remarks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='remarks',
        ),
    ]
