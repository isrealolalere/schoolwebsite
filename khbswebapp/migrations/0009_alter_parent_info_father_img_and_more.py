# Generated by Django 4.2.2 on 2023-06-30 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khbswebapp', '0008_remove_parent_info_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent_info',
            name='father_img',
            field=models.ImageField(null=True, upload_to='media/parent-image/'),
        ),
        migrations.AlterField(
            model_name='parent_info',
            name='mother_img',
            field=models.ImageField(null=True, upload_to='media/parent-image/'),
        ),
        migrations.AlterField(
            model_name='student_reg',
            name='student_img',
            field=models.ImageField(upload_to='media/student-image/'),
        ),
    ]
