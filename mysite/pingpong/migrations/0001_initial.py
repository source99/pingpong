# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_1_score', models.IntegerField(default=0)),
                ('player_2_score', models.IntegerField(default=0)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='match',
            name='player_1_id',
            field=models.ForeignKey(related_name='player_1', to='pingpong.Player', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='player_2_id',
            field=models.ForeignKey(related_name='player_2', to='pingpong.Player', null=True),
            preserve_default=True,
        ),
    ]
