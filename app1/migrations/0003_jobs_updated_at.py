# Generated by Django 5.0.3 on 2024-07-20 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_jobs_category_jobs_gender_jobs_job_type_jobs_max_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
