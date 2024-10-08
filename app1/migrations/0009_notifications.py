# Generated by Django 5.0.3 on 2024-07-23 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_jobapplications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now=True)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
    ]
