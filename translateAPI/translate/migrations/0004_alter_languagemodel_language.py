# Generated by Django 4.0.4 on 2022-04-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0003_alter_languagemodel_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languagemodel',
            name='Language',
            field=models.CharField(max_length=255, verbose_name='A'),
        ),
    ]