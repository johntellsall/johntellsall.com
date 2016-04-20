#!/usr/bin/env python

'''
logquery.py -- expose database queries (SQL)
'''

import functools, os, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings.local'
sys.path.append('project/project')

from meetup.models import Meeting

def output(arg):
    print arg
    print


class LoggingObj(object):
    def __init__(self, other):
        self.other = other

    def log_call(self, ofunc, *args, **kwargs):
        res = ofunc(*args, **kwargs)
        print 'CALL:',ofunc.__name__,args,kwargs
        print '=>',res
        return res
        

    def __getattr__(self, key):
        ofunc = getattr(self.other, key)
        if not callable(ofunc):
            return ofunc
        return functools.partial(self.log_call, ofunc)


qs = Meeting.objects.all()
output( qs.query )


qs = Meeting.objects.all()
qs.query = LoggingObj(qs.query)
output( qs.query.sql_with_params() )

output( list(qs) )
