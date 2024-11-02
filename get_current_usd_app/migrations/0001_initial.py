# Generated by Django 5.1.2 on 2024-11-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=4, max_digits=7, verbose_name='result of rate request')),
                ('request_datetime', models.DateTimeField(verbose_name='request date and time')),
            ],
        ),
    ]