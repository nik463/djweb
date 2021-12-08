# Generated by Django 3.2.9 on 2021-12-05 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employid', models.IntegerField()),
                ('firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('sex', models.CharField(max_length=15)),
                ('position', models.CharField(max_length=30)),
                ('dateofjoin', models.DateField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
