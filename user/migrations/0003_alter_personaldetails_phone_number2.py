# Generated by Django 5.0.4 on 2024-04-13 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_education_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='phone_number2',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
