# Generated by Django 4.2.1 on 2023-06-02 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_socialmedia_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='telegram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
