# Generated by Django 2.1.1 on 2018-09-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(0, 'To do'), (1, 'Done')], default=0)),
            ],
        ),
    ]
