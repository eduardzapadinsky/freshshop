# Generated by Django 4.1.6 on 2023-02-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='url')),
                ('description', models.CharField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('count', models.DecimalField(decimal_places=2, max_digits=7)),
                ('picture', models.ImageField(upload_to='shop_gallery')),
            ],
        ),
    ]
