# Generated by Django 5.1.7 on 2025-03-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DogBoarding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=6)),
                ('capacity', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='boarding_images/')),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
