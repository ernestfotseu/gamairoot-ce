# Generated by Django 2.2.12 on 2022-06-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_etudiants', '0003_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='moyenne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intervals', models.CharField(max_length=100)),
                ('effectif', models.PositiveIntegerField()),
            ],
        ),
    ]
