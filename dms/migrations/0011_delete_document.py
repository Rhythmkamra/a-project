# Generated by Django 4.2.2 on 2024-03-17 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0010_remove_message_remarks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
    ]