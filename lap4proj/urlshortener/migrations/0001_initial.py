# Generated by Django 4.0.3 on 2022-03-30 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shorturl', models.CharField(max_length=20)),
                ('fullurl', models.CharField(max_length=300)),
            ],
        ),
    ]
