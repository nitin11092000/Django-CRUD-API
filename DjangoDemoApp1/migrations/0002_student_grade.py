# Generated by Django 2.2 on 2022-03-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoDemoApp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]