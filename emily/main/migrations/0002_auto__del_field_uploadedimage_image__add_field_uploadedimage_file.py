# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UploadedImage.image'
        db.delete_column('main_uploadedimage', 'image')

        # Adding field 'UploadedImage.file'
        db.add_column('main_uploadedimage', 'file',
                      self.gf('django.db.models.fields.files.ImageField')(default='asd', max_length=100),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'UploadedImage.image'
        raise RuntimeError("Cannot reverse this migration. 'UploadedImage.image' and its values cannot be restored.")
        # Deleting field 'UploadedImage.file'
        db.delete_column('main_uploadedimage', 'file')


    models = {
        'main.uploadedimage': {
            'Meta': {'object_name': 'UploadedImage'},
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']