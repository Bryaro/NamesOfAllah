# Generated by Django 5.1 on 2024-10-13 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('names99', '0002_nameofallah_full_meaning'),
    ]

    operations = [
        migrations.AddField(
            model_name='nameofallah',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='nameofallah',
            name='meaning',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='nameofallah',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
