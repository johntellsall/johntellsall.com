# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Meeting'
        db.create_table(u'meetup_meeting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('meet_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'meetup', ['Meeting'])


    def backwards(self, orm):
        # Deleting model 'Meeting'
        db.delete_table(u'meetup_meeting')


    models = {
        u'meetup.meeting': {
            'Meta': {'object_name': 'Meeting'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meet_date': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['meetup']