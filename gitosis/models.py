from django.contrib.auth.models import User, Group
from django.db import models

"""
[group quux]
members = jdoe wsmith @anothergroup
writable = foo bar baz/thud
readonly = xyzzy

## You can use groups just to avoid listing users multiple times. Note
## no writable= or readonly= lines.
[group anothergroup]
members = alice bill

[repo foo]
## Allow gitweb to show this repository.
gitweb = yes

## Oneline description of the project, mostly for gitweb.
description = blah blah

## Owner of this repository. Used in gitweb list of projects.
owner = John Doe

## Allow git-daemon to publish this repository.
daemon = yes
"""

class GitosisRepo(models.Model):
    
    path = models.CharField(max_length=255, unique=True)
    gitweb = models.BooleanField(default=True)
    description = models.TextField(default='', blank=True)
    owner = models.CharField(max_length=255)
    daemon = models.BooleanField(default=True)
    
    def __unicode__(self):
        return u'%s' % self.path


class GitosisUser(models.Model):
    
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return u'%s' % self.user.username

    
class GitosisGroup(models.Model):
    
    group = models.OneToOneField(Group)
    writable = models.ManyToManyField(GitosisRepo, related_name='writable_by',
        null=True, blank=True)
    readonly = models.ManyToManyField(GitosisRepo, related_name='readable_by',
        null=True, blank=True)
    parent = models.ForeignKey('self', related_name='children', null=True,
        blank=True)
    
    def __unicode__(self):
        return u'%s' % self.group.name
