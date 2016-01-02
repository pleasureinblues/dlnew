# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import product.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand_name', models.CharField(unique=True, max_length=128)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('brand_icon', models.ImageField(upload_to=product.models.update_cat_icon_filename)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(unique=True, max_length=128)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('category_icon', models.ImageField(upload_to=product.models.update_cat_icon_filename)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer_contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.DecimalField(max_digits=15, decimal_places=0)),
                ('subject', models.CharField(max_length=128)),
                ('message', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=128)),
                ('model_name', models.CharField(max_length=128)),
                ('generation', models.CharField(max_length=128)),
                ('processor', models.CharField(max_length=128)),
                ('ram', models.DecimalField(max_digits=2, decimal_places=0)),
                ('hdd', models.DecimalField(max_digits=6, decimal_places=2)),
                ('optical_drive', models.CharField(max_length=128)),
                ('display', models.CharField(max_length=128)),
                ('card_reader', models.CharField(max_length=128)),
                ('blue_tooth', models.CharField(max_length=128)),
                ('web_cam', models.CharField(max_length=128)),
                ('warranty', models.CharField(max_length=128)),
                ('price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('condition', models.TextField()),
                ('product_image', models.ImageField(upload_to=product.models.update_Product_image_filename)),
                ('post_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('brand', models.ForeignKey(to='product.Brand')),
                ('category', models.ForeignKey(to='product.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='customer_contact',
            name='regarding_product',
            field=models.ForeignKey(to='product.ProductProfile'),
            preserve_default=True,
        ),
    ]
