# Generated by Django 2.2.7 on 2021-05-15 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0039_auto_20210514_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
