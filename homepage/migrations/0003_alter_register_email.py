# Generated by Django 4.2.5 on 2023-10-07 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_rename_phonenumber_register_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
