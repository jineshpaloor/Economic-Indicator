# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'EconomicIndicator.history'
        db.delete_column('econ_indicator_economicindicator', 'history_id')

        # Adding field 'History.indicator'
        db.add_column('econ_indicator_history', 'indicator',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['econ_indicator.EconomicIndicator']),
                      keep_default=False)

    def backwards(self, orm):
        # Adding field 'EconomicIndicator.history'
        db.add_column('econ_indicator_economicindicator', 'history',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['econ_indicator.History']),
                      keep_default=False)

        # Deleting field 'History.indicator'
        db.delete_column('econ_indicator_history', 'indicator_id')

    models = {
        'econ_indicator.economicindicator': {
            'Meta': {'object_name': 'EconomicIndicator'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'publish_period': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'econ_indicator.history': {
            'Meta': {'object_name': 'History'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['econ_indicator.EconomicIndicator']"}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'nominal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['econ_indicator']