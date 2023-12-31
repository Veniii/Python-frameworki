# Generated by Django 4.2.6 on 2023-12-06 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingcom_web', '0003_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='imgThumb',
            field=models.ImageField(blank=True, null=True, upload_to='media_ing'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
