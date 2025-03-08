# Generated by Django 5.1.3 on 2025-03-08 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('linkedin_profile', models.URLField()),
                ('personal_statement', models.CharField(max_length=100)),
                ('education', models.TextField()),
                ('work_experience', models.TextField()),
                ('technical_skills', models.TextField()),
                ('soft_skills', models.TextField(blank=True)),
                ('certifications', models.ImageField(blank=True, upload_to='')),
                ('languages', models.TextField(blank=True)),
                ('additional_training', models.TextField(blank=True)),
                ('projects', models.TextField(blank=True)),
                ('volunteer_experience', models.TextField(blank=True)),
            ],
        ),
    ]
