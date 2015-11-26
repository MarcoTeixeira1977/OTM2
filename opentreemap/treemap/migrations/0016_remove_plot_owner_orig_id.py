# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treemap', '0015_auto_20151122_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plot',
            name='owner_orig_id',
        ),
    ]
