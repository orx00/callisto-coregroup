# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-02 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard_builder', '0013_questionpage_to_page_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formquestion',
            name='page',
            field=models.ForeignKey(
                null=True,
                on_delete=models.deletion.SET_NULL,
                to='wizard_builder.Page'),
        ),
        migrations.RemoveField(
            model_name='questionpage',
            name='pagebase_ptr',
        ),
        migrations.RemoveField(
            model_name='questionpage',
            name='sites',
        ),
        migrations.DeleteModel(
            name='QuestionPage',
        ),
        migrations.DeleteModel(
            name='PageBase',
        ),
    ]
