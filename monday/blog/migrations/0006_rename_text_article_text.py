# Generated by Django 4.0 on 2022-01-14 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_person'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Text',
            new_name='text',
        ),
    ]
