from django.contrib.auth.models import User, Group
from django.db import models

"""
Config sections is instances of the appropriate models.
Config is constructing by model managers.

Used sections:
    gitosis  # site dependent 
        daemon
        daemon-if-all
        gitweb
        repositories
        generate-files-in
        ssh-authorized-keys-path
    group <name>
        writable
        readonly
        @todo: map support
        members
    repo <name>
        daemon
        gitweb
        owner
        description
        mirrors
    user <username>
        name  # full name
    mirror <name>
        repos
        uri
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
