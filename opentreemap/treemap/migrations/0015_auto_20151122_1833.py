# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treemap', '0014_tree_data_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plot',
            name='plot_type',
        ),
        migrations.RemoveField(
            model_name='plot',
            name='powerline_conflict_potential',
        ),
        migrations.RemoveField(
            model_name='plot',
            name='sidewalk_damage',
        ),
        migrations.RemoveField(
            model_name='tree',
            name='canopy_condition',
        ),
    ]
