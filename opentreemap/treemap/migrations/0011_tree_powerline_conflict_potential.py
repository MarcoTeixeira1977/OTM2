# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treemap', '0010_tree_canopy_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='powerline_conflict_potential',
            field=models.NullBooleanField(),
        ),
    ]
