# Generated by Django 4.1.2 on 2022-10-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_image_img126_alter_image_img256_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img126',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img512',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]