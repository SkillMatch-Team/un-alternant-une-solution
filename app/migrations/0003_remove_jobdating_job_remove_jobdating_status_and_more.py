# Generated by Django 4.0.3 on 2022-03-18 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobdating',
            name='job',
        ),
        migrations.RemoveField(
            model_name='jobdating',
            name='status',
        ),
        migrations.RemoveField(
            model_name='jobdating',
            name='student',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='JobDating',
        ),
        migrations.DeleteModel(
            name='Profession',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]