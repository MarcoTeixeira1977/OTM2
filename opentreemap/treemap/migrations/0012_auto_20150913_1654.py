# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treemap', '0011_tree_powerline_conflict_potential'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tree',
            name='powerline_conflict_potential',
        ),
        migrations.AddField(
            model_name='plot',
            name='powerline_conflict_potential',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='plot',
            name='sidewalk_damage',
            field=models.NullBooleanField(),
        ),
    ]
