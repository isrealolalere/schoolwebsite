# Generated by Django 4.2.2 on 2023-07-02 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khbswebapp', '0009_alter_parent_info_father_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent_info',
            name='father_img',
            field=models.ImageField(null=True, upload_to='parent-image/'),
        ),
        migrations.AlterField(
            model_name='parent_info',
            name='mother_img',
            field=models.ImageField(null=True, upload_to='parent-image/'),
        ),
        migrations.AlterField(
            model_name='student_reg',
            name='student_img',
            field=models.ImageField(upload_to='student-image/'),
        ),
    ]