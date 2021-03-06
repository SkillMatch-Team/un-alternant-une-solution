# Generated by Django 4.0.3 on 2022-03-24 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0004_school_courses_school_users"),
        ("course", "0002_course_job_codes"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="school",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="course_school+",
                to="authentication.school",
            ),
            preserve_default=False,
        ),
    ]
