# Generated by Django 4.2.3 on 2023-07-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillname', models.CharField(max_length=100)),
                ('skilltype', models.CharField(default='new', max_length=100)),
                ('skillcategory', models.CharField(default='new', max_length=100)),
                ('skillsubcategory', models.CharField(default='new', max_length=100)),
                ('skillmincategory', models.CharField(default='new', max_length=100)),
                ('newskill', models.CharField(default='new', max_length=100)),
                ('skilladdess', models.CharField(default='description', max_length=1000)),
            ],
        ),
    ]
