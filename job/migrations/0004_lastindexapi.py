# Generated by Django 4.0.3 on 2022-03-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_jobcode_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastIndexApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_index', models.IntegerField()),
            ],
            options={
                'db_table': 'last_index_api',
            },
        ),
    ]
