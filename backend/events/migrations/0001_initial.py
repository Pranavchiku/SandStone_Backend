# Generated by Django 4.1.1 on 2022-09-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker_name', models.CharField(max_length=100)),
                ('speaker_company', models.CharField(max_length=100)),
                ('speaker_position', models.CharField(max_length=100)),
                ('speaker_date', models.DateField()),
            ],
        ),
    ]
