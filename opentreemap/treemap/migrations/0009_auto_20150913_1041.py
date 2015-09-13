# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_cot_num(apps, schema_editor):
    """City of Tampa uses the ID (pk) from the OTM1 DB
    This data migration function will eventually
    copy those IDs into a new field: cot_tree_num
    
    """
    pass
    


class Migration(migrations.Migration):

    dependencies = [
        ('treemap', '0008_tree_cot_tree_num'),
    ]

    operations = [

            migrations.RunPython(add_cot_num),
    ]
