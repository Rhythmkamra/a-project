# Generated by Django 4.2.2 on 2024-03-13 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0008_alter_message_message_alter_message_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='remarks',
            field=models.FileField(upload_to='remarks/'),
        ),
    ]