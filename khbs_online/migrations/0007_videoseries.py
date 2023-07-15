# Generated by Django 4.2.2 on 2023-07-07 09:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('khbs_online', '0006_program_date_field_specialprogram_date_field_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('video_file', models.FileField(null=True, upload_to='special_videos_uploaded/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_series', to='khbs_online.specialprogram')),
            ],
        ),
    ]
