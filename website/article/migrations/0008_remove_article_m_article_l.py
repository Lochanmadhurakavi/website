# Generated by Django 4.1.1 on 2022-09-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_remove_article_l_article_m'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='M',
        ),
        migrations.AddField(
            model_name='article',
            name='L',
            field=models.CharField(choices=[('11', 'AC Fail Window')], max_length=20, null=True),
        ),
    ]
