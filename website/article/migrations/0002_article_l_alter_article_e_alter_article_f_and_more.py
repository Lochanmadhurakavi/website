# Generated by Django 4.1.1 on 2022-09-20 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='L',
            field=models.CharField(choices=[('11', 'AC Fail Window')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='E',
            field=models.CharField(choices=[('4', '4'), ('8', '8'), ('16', '16'), ('32', '32'), ('64', '64')], max_length=2),
        ),
        migrations.AlterField(
            model_name='article',
            name='F',
            field=models.CharField(choices=[('X', 'X'), ('Y', 'Y'), ('Z', 'Z')], max_length=2),
        ),
        migrations.AlterField(
            model_name='article',
            name='G',
            field=models.CharField(choices=[('U', 'U'), ('D', 'D')], max_length=2),
        ),
        migrations.AlterField(
            model_name='article',
            name='H',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I')], max_length=2),
        ),
        migrations.AlterField(
            model_name='article',
            name='I',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], max_length=2),
        ),
        migrations.AlterField(
            model_name='article',
            name='J',
            field=models.CharField(choices=[('12', 'DC Fail Window N')], max_length=20),
        ),
        migrations.AlterField(
            model_name='article',
            name='K',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], max_length=2),
        ),
    ]