# Generated by Django 4.0 on 2022-01-31 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_article_author_alter_article_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
