# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20160126_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_ps_contact',
            name='email',
            field=models.EmailField(max_length=75),
        ),
        migrations.AlterField(
            model_name='customer_ps_contact',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='customer_ps_contact',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='customer_ps_contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
        migrations.AlterField(
            model_name='customer_ps_contact',
            name='product',
            field=models.ForeignKey(to='product.ProductProfile'),
        ),
        migrations.AlterField(
            model_name='customer_ps_contact',
            name='subject',
            field=models.CharField(max_length=128),
        ),
    ]
