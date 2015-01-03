# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.db.models.query import QuerySet
from django.db.models import Count
from model_utils.managers import PassThroughManager
from django.contrib.auth.models import UserManager

class UserQuerySet(QuerySet):
    def for_user(self, user):
        print "A:", user.has_perm('users.can_view_other')
        if not user.has_perm('users.can_view_other'):
            return self.filter(Q(username=user.username) | Q(is_staff=True))
        return self

    def with_case_count(self):
        return self.annotate(case_count=Count('case'))

class UserManager(UserManager):  # TODO: How to write more DRY?
    def get_queryset(self):
        return UserQuerySet(self.model)

    def for_user(self, user):
        return self.get_query_set().for_user(user)

    def with_case_count(self):
        return self.get_query_set().with_case_count()


class User(AbstractUser):
    objects = UserManager()

    def __unicode__(self):
        if self.first_name or self.last_name:
            return "{0} {1}".format(self.first_name, self.last_name)
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    class Meta:
        permissions = (("can_view_other", "Can view other"),)
