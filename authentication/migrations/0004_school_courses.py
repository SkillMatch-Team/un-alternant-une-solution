# Generated by Django 4.0.3 on 2022-03-18 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_create_at_course_update_at'),
        ('authentication', '0003_alter_school_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='courses',
            field=models.ManyToManyField(related_name='school_courses+', to='course.course'),
        ),
    ]
