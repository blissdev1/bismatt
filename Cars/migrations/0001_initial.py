# Generated by Django 4.2.1 on 2023-06-29 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True, blank=True, null=True)),
                ('model', models.CharField(max_length=200)),
                ('cat', models.CharField(blank=True, max_length=120, null=True)),
                ('vin', models.CharField(blank=True, max_length=200, null=True)),
                ('mileage', models.CharField(blank=True, max_length=200, null=True)),
                ('condition', models.TextField(blank=True, default='good', null=True)),
                ('interior_color', models.CharField(blank=True, max_length=120, null=True)),
                ('exterior_color', models.CharField(blank=True, max_length=120, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='./uploaded_img')),
                ('imga', models.ImageField(blank=True, null=True, upload_to='./uploaded_img')),
                ('imgb', models.ImageField(blank=True, null=True, upload_to='./uploaded_img')),
                ('imgc', models.ImageField(blank=True, null=True, upload_to='./uploaded_img')),
                ('imgd', models.ImageField(blank=True, null=True, upload_to='./uploaded_img')),
                ('transittion', models.CharField(blank=True, max_length=200, null=True)),
                ('horsepower', models.CharField(blank=True, max_length=200, null=True)),
                ('torque', models.CharField(blank=True, max_length=200, null=True)),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cars.maker')),
            ],
        ),
    ]
