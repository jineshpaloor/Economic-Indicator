# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'History'
        db.create_table('econ_indicator_history', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('month', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('nominal', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('econ_indicator', ['History'])

        # Adding model 'EconomicIndicator'
        db.create_table('econ_indicator_economicindicator', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('long_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('publish_period', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('parent_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('history', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['econ_indicator.History'])),
        ))
        db.send_create_signal('econ_indicator', ['EconomicIndicator'])

    def backwards(self, orm):
        # Deleting model 'History'
        db.delete_table('econ_indicator_history')

        # Deleting model 'EconomicIndicator'
        db.delete_table('econ_indicator_economicindicator')

    models = {
        'econ_indicator.economicindicator': {
            'Meta': {'object_name': 'EconomicIndicator'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'history': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['econ_indicator.History']"}),
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
            'month': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'nominal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['econ_indicator']