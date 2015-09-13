# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treemap', '0012_auto_20150913_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='plot_type',
            field=models.CharField(blank=True, 
                                   max_length=256, 
                                   null=True, 
                                   choices=[
                                       ('1', 'Well/Pit'), 
                                       ('2', 'Median/Island'), 
                                       ('3', 'Tree Lawn'), 
                                       ('4', 'Park'), 
                                       ('5', 'Planter'), 
                                       ('6', 'Other'), 
                                       ('7', 'Yard'), 
                                       ('8', 'Natural Area')]),
        ),
    ]
