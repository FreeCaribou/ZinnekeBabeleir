# Generated by Django 3.1.6 on 2021-12-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_auto_20210328_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legislature',
            name='parliament',
            field=models.CharField(choices=[('FED', 'federal'), ('BRU', 'brussels'), ('VLA', 'vlaams'), ('WAL', 'wallonia'), ('FRA', 'francophone'), ('GER', 'germanophone'), ('SEN', 'senat'), ('other', 'other')], default='other', max_length=10),
        ),
    ]
