# Generated by Django 4.2.4 on 2023-08-24 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khbswebapp', '0010_alter_parent_info_father_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]