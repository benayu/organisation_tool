# Generated by Django 4.1.1 on 2022-09-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-date_uploaded']},
        ),
        migrations.AddField(
            model_name='photo',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]