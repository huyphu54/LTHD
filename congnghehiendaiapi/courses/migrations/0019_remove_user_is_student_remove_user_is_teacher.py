# Generated by Django 4.2.13 on 2024-06-15 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_rename_hocvi_user_degree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_teacher',
        ),
    ]