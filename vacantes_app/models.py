# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField


class Vacantes(models.Model):
	LANGUAGES = (
	    ('es', u'Español'),
	    ('en', u'Inglés'),
	)
	is_active = models.BooleanField()
	position = models.CharField()
	descripion = HTMLField()
	skills = HTMLField()
	lang = models.CharField(max_length=1, choices=LANGUAGES)
	date = models.DateTimeField()

	class Meta:
		db_table = 'po_vacancy'