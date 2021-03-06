# Generated by Django 2.0 on 2018-09-11 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name='URL à réduire')),
                ('code', models.CharField(max_length=7, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name="Date d'enregistrement")),
                ('pseudo', models.CharField(blank=True, max_length=255, null=True)),
                ('nb_acces', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '< Mini URL >',
                'verbose_name_plural': '< Minis URL >',
            },
        ),
    ]
