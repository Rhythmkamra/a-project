# Generated by Django 4.2.2 on 2024-02-26 12:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0002_remove_document_content_remove_document_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='document',
        ),
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(default=0, upload_to='documents/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='remarks',
            field=models.TextField(blank=True),
        ),
    ]