# Generated by Django 3.1.3 on 2020-12-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20201219_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=50)),
                ('field2', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('field1', 'field2')},
            },
        ),
    ]
