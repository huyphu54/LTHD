# Generated by Django 4.2.13 on 2024-06-15 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_remove_evaluationcriterion_curriculum_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='HocVi',
            new_name='degree',
        ),
    ]