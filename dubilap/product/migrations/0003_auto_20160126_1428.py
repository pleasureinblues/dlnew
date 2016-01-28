# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20151226_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_ps_contact',
            name='email',
            field=models.EmailField(help_text=b'Email', max_length=75),
        ),
        migrations.AlterField(
            model_name='customer_ps_contact',
            name='message',
            field=models.TextField(help_text=b'Message'),
        ),
        migrations.AlterField(
            model_name='customer_ps_contact',
            name='name',
            field=models.CharField(help_text=b'Name', max_length=128),
        ),
        migrations.AlterField(
            model_name='customer_ps_contact',
            name='phone_number',
            field=models.CharField(blank=True, help_text=b'Phone Number', max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
        migrations.AlterField(
            model_name='customer_ps_contact',
            name='product',
            field=models.ForeignKey(help_text=b'Product', to='product.ProductProfile'),
        ),
        migrations.AlterField(
            model_name='customer_ps_contact',
            name='subject',
            field=models.CharField(help_text=b'Subject', max_length=128),
        ),
    ]
