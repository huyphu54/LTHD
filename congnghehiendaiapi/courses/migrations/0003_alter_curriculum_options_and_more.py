# Generated by Django 4.2.13 on 2024-05-28 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_category_alter_comment_options_alter_course_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curriculum',
            options={'permissions': [('can_add_curriculum', 'Can add curriculum'), ('can_view_curriculum', 'Can view curriculum')]},
        ),
        migrations.RenameField(
            model_name='curriculum',
            old_name='teacher',
            new_name='user',
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.category'),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curriculums', to='courses.course'),
        ),
    ]