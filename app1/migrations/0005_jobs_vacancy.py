# Generated by Django 5.0.3 on 2024-07-20 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_jobs_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='vacancy',
            field=models.IntegerField(null=True),
        ),
    ]
