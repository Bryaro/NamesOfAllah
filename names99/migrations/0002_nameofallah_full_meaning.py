# Generated by Django 5.1 on 2024-10-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('names99', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nameofallah',
            name='full_meaning',
            field=models.TextField(default='Meaning not yet added.'),
            preserve_default=False,
        ),
    ]
