# Generated by Django 3.0.7 on 2020-07-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=11)),
                ('date_time', models.DateTimeField(blank=True)),
            ],
        ),
    ]
