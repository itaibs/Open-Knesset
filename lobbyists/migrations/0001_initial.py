# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LobbyistHistory'
        db.create_table(u'lobbyists_lobbyisthistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scrape_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'lobbyists', ['LobbyistHistory'])

        # Adding M2M table for field lobbyists on 'LobbyistHistory'
        m2m_table_name = db.shorten_name(u'lobbyists_lobbyisthistory_lobbyists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lobbyisthistory', models.ForeignKey(orm[u'lobbyists.lobbyisthistory'], null=False)),
            ('lobbyist', models.ForeignKey(orm[u'lobbyists.lobbyist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['lobbyisthistory_id', 'lobbyist_id'])

        # Adding model 'Lobbyist'
        db.create_table(u'lobbyists_lobbyist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='lobbyist', null=True, to=orm['persons.Person'])),
            ('source_id', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'lobbyists', ['Lobbyist'])

        # Adding model 'LobbyistData'
        db.create_table(u'lobbyists_lobbyistdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lobbyist', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='data', null=True, to=orm['lobbyists.Lobbyist'])),
            ('scrape_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('family_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('profession', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('corporation_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('corporation_id', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('faction_member', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('faction_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('permit_type', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'lobbyists', ['LobbyistData'])

        # Adding M2M table for field represents on 'LobbyistData'
        m2m_table_name = db.shorten_name(u'lobbyists_lobbyistdata_represents')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lobbyistdata', models.ForeignKey(orm[u'lobbyists.lobbyistdata'], null=False)),
            ('lobbyistrepresent', models.ForeignKey(orm[u'lobbyists.lobbyistrepresent'], null=False))
        ))
        db.create_unique(m2m_table_name, ['lobbyistdata_id', 'lobbyistrepresent_id'])

        # Adding model 'LobbyistRepresent'
        db.create_table(u'lobbyists_lobbyistrepresent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source_id', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'lobbyists', ['LobbyistRepresent'])

        # Adding model 'LobbyistRepresentData'
        db.create_table(u'lobbyists_lobbyistrepresentdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lobbyist_represent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='data', null=True, to=orm['lobbyists.LobbyistRepresent'])),
            ('scrape_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'lobbyists', ['LobbyistRepresentData'])


    def backwards(self, orm):
        # Deleting model 'LobbyistHistory'
        db.delete_table(u'lobbyists_lobbyisthistory')

        # Removing M2M table for field lobbyists on 'LobbyistHistory'
        db.delete_table(db.shorten_name(u'lobbyists_lobbyisthistory_lobbyists'))

        # Deleting model 'Lobbyist'
        db.delete_table(u'lobbyists_lobbyist')

        # Deleting model 'LobbyistData'
        db.delete_table(u'lobbyists_lobbyistdata')

        # Removing M2M table for field represents on 'LobbyistData'
        db.delete_table(db.shorten_name(u'lobbyists_lobbyistdata_represents'))

        # Deleting model 'LobbyistRepresent'
        db.delete_table(u'lobbyists_lobbyistrepresent')

        # Deleting model 'LobbyistRepresentData'
        db.delete_table(u'lobbyists_lobbyistrepresentdata')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'lobbyists.lobbyist': {
            'Meta': {'object_name': 'Lobbyist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'lobbyist'", 'null': 'True', 'to': u"orm['persons.Person']"}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'lobbyists.lobbyistdata': {
            'Meta': {'object_name': 'LobbyistData'},
            'corporation_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'corporation_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'faction_member': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'faction_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lobbyist': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'data'", 'null': 'True', 'to': u"orm['lobbyists.Lobbyist']"}),
            'permit_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'represents': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lobbyists.LobbyistRepresent']", 'symmetrical': 'False'}),
            'scrape_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'lobbyists.lobbyisthistory': {
            'Meta': {'object_name': 'LobbyistHistory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lobbyists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lobbyists.Lobbyist']", 'symmetrical': 'False'}),
            'scrape_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'lobbyists.lobbyistrepresent': {
            'Meta': {'object_name': 'LobbyistRepresent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'lobbyists.lobbyistrepresentdata': {
            'Meta': {'object_name': 'LobbyistRepresentData'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lobbyist_represent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'data'", 'null': 'True', 'to': u"orm['lobbyists.LobbyistRepresent']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'scrape_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'mks.knesset': {
            'Meta': {'object_name': 'Knesset'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'mks.member': {
            'Meta': {'ordering': "['name']", 'object_name': 'Member'},
            'area_of_residence': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'average_monthly_committee_presence': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'average_weekly_presence_hours': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'backlinks_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'bills_stats_approved': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bills_stats_first': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bills_stats_pre': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bills_stats_proposed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'blog': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['planet.Blog']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'current_party': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'members'", 'null': 'True', 'to': u"orm['mks.Party']"}),
            'current_position': ('django.db.models.fields.PositiveIntegerField', [], {'default': '999', 'blank': 'True'}),
            'current_role_descriptions': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_death': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'family_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'is_current': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'number_of_children': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parties': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'all_members'", 'symmetrical': 'False', 'through': u"orm['mks.Membership']", 'to': u"orm['mks.Party']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'place_of_residence': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'place_of_residence_lat': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'place_of_residence_lon': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'residence_centrality': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'residence_economy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'year_of_aliyah': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'mks.membership': {
            'Meta': {'object_name': 'Membership'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mks.Member']"}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mks.Party']"}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': '999', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'mks.party': {
            'Meta': {'ordering': "('-number_of_seats',)", 'unique_together': "(('knesset', 'name'),)", 'object_name': 'Party'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_coalition': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'knesset': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parties'", 'null': 'True', 'to': u"orm['mks.Knesset']"}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'number_of_members': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_seats': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'persons.person': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Person'},
            'area_of_residence': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_death': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'family_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'mk': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'person'", 'null': 'True', 'to': u"orm['mks.Member']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'number_of_children': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'place_of_residence': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'place_of_residence_lat': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'place_of_residence_lon': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'residence_centrality': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'residence_economy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'titles': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'persons'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['persons.Title']"}),
            'year_of_aliyah': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'persons.title': {
            'Meta': {'object_name': 'Title'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'planet.blog': {
            'Meta': {'ordering': "('title', 'url')", 'object_name': 'Blog'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '1024', 'db_index': 'True'})
        }
    }

    complete_apps = ['lobbyists']