# Generated by Django 5.1.3 on 2024-12-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='problems',
            field=models.ManyToManyField(related_name='categories', to='problem_management.problem'),
        ),
    ]