# Generated by Django 3.2.15 on 2023-02-14 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230213_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='documenti_user', verbose_name='File Auto'),
        ),
    ]