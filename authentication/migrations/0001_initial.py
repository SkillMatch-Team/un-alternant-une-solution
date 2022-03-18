# Generated by Django 4.0.3 on 2022-03-18 10:11

import authentication.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.CharField(max_length=75, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='Email')),
                ('first_name', models.CharField(max_length=75, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=75, verbose_name='Last Name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', authentication.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Company Name')),
                ('description', models.TextField(null=True, verbose_name='Company Description')),
                ('city', models.CharField(max_length=75, null=True, verbose_name='City')),
                ('street', models.CharField(max_length=75, null=True, verbose_name='Street')),
                ('zip_code', models.CharField(max_length=75, null=True, verbose_name='Zip Code')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(null=True, verbose_name='Birthday')),
                ('linkedin_url', models.URLField(null=True, verbose_name='LinkedIn URL')),
                ('cv_path', models.CharField(max_length=255, null=True, verbose_name='CV Path')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='School Name')),
                ('description', models.TextField(null=True, verbose_name='School Description')),
                ('city', models.CharField(max_length=75, verbose_name='City')),
                ('street', models.CharField(max_length=75, verbose_name='Street')),
                ('zip_code', models.CharField(max_length=75, verbose_name='Zip Code')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
