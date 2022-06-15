# Generated by Django 3.2.6 on 2022-06-13 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0004_answers_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Question',
            new_name='question',
        ),
        migrations.AlterField(
            model_name='question',
            name='cognitive_level',
            field=models.CharField(choices=[('Hard', 'Hard'), ('Easy', 'Easy'), ('Medium', 'Medium')], default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('Fill_in_the_blanks', 'Fill_in_the_blanks'), ('MCQ', 'MCQ'), ('Match_the_following', 'Match_the_following')], default='0', max_length=20),
        ),
    ]