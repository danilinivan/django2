# Generated by Django 4.0 on 2022-01-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_text_article_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='image.jpeg', upload_to=''),
        ),
    ]