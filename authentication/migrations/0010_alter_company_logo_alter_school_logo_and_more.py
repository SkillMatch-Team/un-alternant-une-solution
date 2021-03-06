# Generated by Django 4.0.3 on 2022-03-31 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0009_remove_user_cv_student_cv"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="logo",
            field=models.ImageField(
                blank=True, null=True, upload_to="authentication/files/picture/company"
            ),
        ),
        migrations.AlterField(
            model_name="school",
            name="logo",
            field=models.ImageField(
                blank=True, null=True, upload_to="authentication/files/picture/school"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="cv",
            field=models.FileField(
                blank=True, null=True, upload_to="authentication/files/cv"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="logo",
            field=models.ImageField(
                blank=True, null=True, upload_to="authentication/files/picture"
            ),
        ),
    ]
