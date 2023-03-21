# Generated by Django 4.1.6 on 2023-03-17 04:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('products', models.ManyToManyField(to='crud.product')),
            ],
        ),
    ]
