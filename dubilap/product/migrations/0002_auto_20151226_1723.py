# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_ps_contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=75)),
                ('subject', models.CharField(max_length=128)),
                ('message', models.TextField()),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('product', models.ForeignKey(to='product.ProductProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='customer_contact',
            name='regarding_product',
        ),
        migrations.DeleteModel(
            name='Customer_contact',
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_icon',
            field=models.ImageField(upload_to=product.models.update_brand_icon_filename),
        ),
    ]
