# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treemap', '0009_auto_20150913_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='canopy_condition',
            field=models.CharField(blank=True, 
                                   max_length=256, 
                                   null=True, 
                                   choices=[('1', 'Full - No Gaps'), 
                                            ('2', 'Small Gaps (up to 25% missing)'), 
                                            ('3', 'Moderate Gaps (up to 50% missing)'), 
                                            ('4', 'Large Gaps (up to 75% missing)'), 
                                            ('5', 'Little or None (up to 100% missing)')]),
        ),
    ]
