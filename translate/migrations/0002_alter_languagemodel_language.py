# Generated by Django 4.0.4 on 2022-04-14 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languagemodel',
            name='Language',
            field=models.CharField(max_length=300, verbose_name='Language'),
        ),
    ]
