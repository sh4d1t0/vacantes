# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField


class Vacantes(models.Model):
	LANGUAGES = (
	    ('es', 'es'),
	    ('en', 'en'),
	)
	is_active = models.BooleanField()
	position = models.CharField(max_length=150)
	description = HTMLField()
	skills = HTMLField()
	lang = models.CharField(max_length=5, choices=LANGUAGES)
	date = models.DateTimeField()

	def __unicode__(self):
		return self.position

	class Meta:
		db_table = 'po_vacancy'