# Generated by Django 5.0.4 on 2024-04-13 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_personaldetails_phone_number2'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(default='website', max_length=200),
        ),
    ]
