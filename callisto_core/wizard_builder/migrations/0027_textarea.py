# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 16:12
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callisto_core.wizard_builder', '0026_remove_page_infobox'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextArea',
            fields=[
                ('formquestion_ptr',
                 models.OneToOneField(
                     auto_created=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     parent_link=True,
                     primary_key=True,
                     serialize=False,
                     to='wizard_builder.FormQuestion')),
            ],
            bases=(
                'wizard_builder.formquestion',
            ),
        ),
    ]