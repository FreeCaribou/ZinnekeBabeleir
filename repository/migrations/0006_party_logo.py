# Generated by Django 3.1.6 on 2021-12-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_auto_20211206_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='logo',
            field=models.BinaryField(default=0, editable=True),
        ),
    ]
