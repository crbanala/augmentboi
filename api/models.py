from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):

	user = models.OneToOneField(User, primary_key = True, db_column = 'user_id', on_delete = models.CASCADE)
	class Meta:
		db_table = 'customer'
	def __unicode__(self):
		return unicode(self.user)
