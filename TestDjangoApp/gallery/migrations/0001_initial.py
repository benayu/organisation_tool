# Generated by Django 4.1.1 on 2022-09-14 21:45

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('photo', models.ImageField(upload_to='uploads')),
                ('date_uploaded', models.DateTimeField(auto_now=True)),
                ('favorite', models.BooleanField(default=False)),
            ],
            managers=[
                ('gallery', django.db.models.manager.Manager()),
            ],
        ),
    ]