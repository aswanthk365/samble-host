# Generated by Django 3.1.7 on 2023-12-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_remove_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-12-08'),
            preserve_default=False,
        ),
    ]
