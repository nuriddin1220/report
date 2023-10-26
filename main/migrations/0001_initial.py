# Generated by Django 4.2.6 on 2023-10-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reports',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('report_name', models.CharField(max_length=4000)),
                ('report_type', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'reports',
                'managed': True,
            },
        ),
    ]
