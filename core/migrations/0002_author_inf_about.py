# Generated by Django 4.2.1 on 2023-05-10 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='inf_about',
            field=models.TextField(default=111, help_text='Краткая информация об авторе', max_length=2550),
            preserve_default=False,
        ),
    ]
