# Generated by Django 5.0.4 on 2024-10-27 07:46

import django.core.validators
import furry_funnies.author.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(4), furry_funnies.author.validators.letters_validator])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2), furry_funnies.author.validators.letters_validator])),
                ('passcode', models.CharField(help_text='Your passcode must be a combination of 6 digits', validators=[django.core.validators.MinLengthValidator(6, 'Your passcode must be exactly 6 digits!'), django.core.validators.MaxLengthValidator(6, 'Your passcode must be exactly 6 digits!'), furry_funnies.author.validators.passcode_validator])),
                ('pets_number', models.PositiveSmallIntegerField()),
                ('info', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]