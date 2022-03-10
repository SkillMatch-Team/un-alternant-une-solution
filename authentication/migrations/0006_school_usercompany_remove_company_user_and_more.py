# Generated by Django 4.0.3 on 2022-03-10 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='School Name')),
                ('city', models.CharField(max_length=75, verbose_name='City')),
                ('street', models.CharField(max_length=75, verbose_name='Street')),
                ('zip_code', models.CharField(max_length=75, verbose_name='Zip Code')),
            ],
            options={
                'db_table': 'school',
            },
        ),
        migrations.CreateModel(
            name='UserCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'user_company',
            },
        ),
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.AddField(
            model_name='company',
            name='userCompanies',
            field=models.ManyToManyField(through='authentication.UserCompany', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=1, max_length=75, verbose_name='First Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=1, max_length=75, verbose_name='Last Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='UserSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.school')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_school',
            },
        ),
        migrations.AddField(
            model_name='usercompany',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.company'),
        ),
        migrations.AddField(
            model_name='usercompany',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='school',
            name='userSchools',
            field=models.ManyToManyField(through='authentication.UserSchool', to=settings.AUTH_USER_MODEL),
        ),
    ]
