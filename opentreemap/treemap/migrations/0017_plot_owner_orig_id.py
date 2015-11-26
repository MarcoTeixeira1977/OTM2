# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treemap', '0016_remove_plot_owner_orig_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='owner_orig_id',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
