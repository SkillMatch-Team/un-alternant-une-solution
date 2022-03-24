# Generated by Django 4.0.3 on 2022-03-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_company'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='job_codes',
            field=models.ManyToManyField(related_name='course_job_codes+', to='job.jobcode'),
        ),
    ]
