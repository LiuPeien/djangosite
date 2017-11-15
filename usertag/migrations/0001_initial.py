# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-15 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cds',
            fields=[
                ('cd_id', models.BigIntegerField(db_column='CD_ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'CDS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ColumnLabel',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('db_name', models.CharField(max_length=255)),
                ('table_name', models.CharField(max_length=255)),
                ('column_name', models.CharField(max_length=255)),
                ('join_column_name', models.CharField(max_length=255)),
                ('type', models.IntegerField()),
                ('aggregate_rule', models.CharField(max_length=255)),
                ('aggregate_express', models.CharField(max_length=255)),
                ('classification', models.IntegerField()),
                ('column_enums', models.CharField(max_length=2000)),
                ('note', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'column_label',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ColumnsV2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, db_column='COMMENT', max_length=256, null=True)),
                ('column_name', models.CharField(db_column='COLUMN_NAME', max_length=767)),
                ('type_name', models.CharField(blank=True, db_column='TYPE_NAME', max_length=4000, null=True)),
                ('integer_idx', models.IntegerField(db_column='INTEGER_IDX')),
            ],
            options={
                'db_table': 'COLUMNS_V2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dbs',
            fields=[
                ('db_id', models.BigIntegerField(db_column='DB_ID', primary_key=True, serialize=False)),
                ('desc', models.CharField(blank=True, db_column='DESC', max_length=4000, null=True)),
                ('db_location_uri', models.CharField(db_column='DB_LOCATION_URI', max_length=4000)),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=128, null=True, unique=True)),
                ('owner_name', models.CharField(blank=True, db_column='OWNER_NAME', max_length=128, null=True)),
                ('owner_type', models.CharField(blank=True, db_column='OWNER_TYPE', max_length=10, null=True)),
            ],
            options={
                'db_table': 'DBS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sds',
            fields=[
                ('sd_id', models.BigIntegerField(db_column='SD_ID', primary_key=True, serialize=False)),
                ('input_format', models.CharField(blank=True, db_column='INPUT_FORMAT', max_length=4000, null=True)),
                ('is_compressed', models.TextField(db_column='IS_COMPRESSED')),
                ('is_storedassubdirectories', models.TextField(db_column='IS_STOREDASSUBDIRECTORIES')),
                ('location', models.CharField(blank=True, db_column='LOCATION', max_length=4000, null=True)),
                ('num_buckets', models.IntegerField(db_column='NUM_BUCKETS')),
                ('output_format', models.CharField(blank=True, db_column='OUTPUT_FORMAT', max_length=4000, null=True)),
            ],
            options={
                'db_table': 'SDS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Serdes',
            fields=[
                ('serde_id', models.BigIntegerField(db_column='SERDE_ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=128, null=True)),
                ('slib', models.CharField(blank=True, db_column='SLIB', max_length=4000, null=True)),
            ],
            options={
                'db_table': 'SERDES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbls',
            fields=[
                ('tbl_id', models.BigIntegerField(db_column='TBL_ID', primary_key=True, serialize=False)),
                ('create_time', models.IntegerField(db_column='CREATE_TIME')),
                ('last_access_time', models.IntegerField(db_column='LAST_ACCESS_TIME')),
                ('owner', models.CharField(blank=True, db_column='OWNER', max_length=767, null=True)),
                ('retention', models.IntegerField(db_column='RETENTION')),
                ('tbl_name', models.CharField(blank=True, db_column='TBL_NAME', max_length=128, null=True)),
                ('tbl_type', models.CharField(blank=True, db_column='TBL_TYPE', max_length=128, null=True)),
                ('view_expanded_text', models.TextField(blank=True, db_column='VIEW_EXPANDED_TEXT', null=True)),
                ('view_original_text', models.TextField(blank=True, db_column='VIEW_ORIGINAL_TEXT', null=True)),
            ],
            options={
                'db_table': 'TBLS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField()),
                ('user_identity_column', models.CharField(max_length=255)),
                ('last_time_type', models.IntegerField()),
                ('note', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'user_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserGroupColumnLabelRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.BigIntegerField()),
                ('label_id', models.BigIntegerField()),
                ('express', models.CharField(max_length=255)),
                ('and_or_type', models.IntegerField()),
                ('note', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'user_group_column_label_relation',
                'managed': False,
            },
        ),
    ]
