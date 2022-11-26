# Generated by Django 2.2.12 on 2022-06-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_etudiants', '0004_moyenne'),
    ]

    operations = [
        migrations.CreateModel(
            name='moyenneE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intervals', models.CharField(max_length=100)),
                ('effectif', models.PositiveIntegerField()),
                ('effectif1', models.PositiveIntegerField()),
                ('effectif2', models.PositiveIntegerField()),
                ('effectif3', models.PositiveIntegerField()),
                ('effectif4', models.PositiveIntegerField()),
                ('effectif5', models.PositiveIntegerField()),
            ],
        ),
    ]
