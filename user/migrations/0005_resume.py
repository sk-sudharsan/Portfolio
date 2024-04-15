# Generated by Django 5.0.4 on 2024-04-13 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_project_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cv', models.ImageField(upload_to='resumes/')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.personaldetails')),
            ],
        ),
    ]
