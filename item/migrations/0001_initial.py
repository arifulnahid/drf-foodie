# Generated by Django 5.0.6 on 2024-07-08 04:11

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('image', models.ImageField(upload_to='uploads/')),
                ('is_special', models.BooleanField(default=False)),
                ('discount', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MinValueValidator(100)])),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.category')),
            ],
        ),
    ]