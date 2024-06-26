# Generated by Django 4.2.13 on 2024-06-19 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_alter_evaluationcriterion_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curriculum',
            options={'permissions': [('can_add_curriculum', 'Can add curriculum'), ('can_view_curriculum', 'Can view cusrriculum')]},
        ),
        migrations.AlterModelOptions(
            name='evaluationcriterion',
            options={'ordering': ['-id']},
        ),
        migrations.AlterUniqueTogether(
            name='curriculumevaluation',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='evaluationcriterion',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='curriculum',
        ),
        migrations.AddField(
            model_name='comment',
            name='syllabus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.syllabus'),
        ),
        migrations.AddField(
            model_name='curriculumevaluation',
            name='syllabus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.syllabus'),
        ),
        migrations.AddField(
            model_name='evaluationcriterion',
            name='curriculum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.curriculum'),
        ),
        migrations.AlterUniqueTogether(
            name='curriculumevaluation',
            unique_together={('syllabus', 'evaluation_criterion')},
        ),
        migrations.RemoveField(
            model_name='curriculumevaluation',
            name='curriculum',
        ),
        migrations.RemoveField(
            model_name='evaluationcriterion',
            name='course',
        ),
    ]
