# Generated by Django 4.2.1 on 2023-06-02 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_student_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
    ]
