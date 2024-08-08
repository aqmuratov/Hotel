# Generated by Django 4.2 on 2024-08-06 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klas', models.CharField(max_length=255, verbose_name='Hoteldin kategoriyalari: ')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Hoteldin slugi: ')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=255, verbose_name='Hoteldin ati: ')),
                ('adress', models.CharField(max_length=255, verbose_name='Hoteldin adresi: ')),
                ('baxasi', models.DecimalField(decimal_places=1, max_digits=10, verbose_name='Hoteldin 1 kunlik cenasi: ')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='hotels', verbose_name='Hoteldin suwreti 1: ')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='hotels', verbose_name='Hoteldin suwreti 2: ')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='hotels', verbose_name='Hoteldin suwreti 3: ')),
                ('klas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotelcategory', verbose_name='Hoteldin kategoriyalari: ')),
            ],
        ),
    ]
