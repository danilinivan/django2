# Generated by Django 4.0 on 2022-01-12 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]