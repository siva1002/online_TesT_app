# Generated by Django 3.2.6 on 2022-06-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('is_admin', 'is_admin'), ('is_staff', 'is_staff'), ('is_student', 'is_student')], default='0', max_length=20),
        ),
    ]