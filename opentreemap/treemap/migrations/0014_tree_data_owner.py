# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('treemap', '0013_plot_plot_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='data_owner',
            field=models.ForeignKey(related_name='owner', 
                                    blank=True, 
                                    to=settings.AUTH_USER_MODEL, 
                                    null=True),
        ),
    ]
