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


class Aggregate(object):
    def __init__(self, other):
        self.other = other


    def ag_call(self, res, ofunc, args, kwargs): # pylint: disable=W0613
        raise NotImplementedError()
        

    def __getattr__(self, key):
        ovalue = getattr(self.other, key)
        if not callable(ovalue):
            print 'ATTR:', key, ovalue
            return ovalue
        def ag_divert(*args, **kwargs):
            res = ovalue(*args, **kwargs),
            self.ag_call(res, ovalue, args, kwargs)
            return res
        return ag_divert


class LoggingAg(Aggregate):

    def ag_call(self, res, ofunc, *args, **kwargs):
        print 'CALL:', ofunc.__name__, args, kwargs
        print '=>', res


qs = Meeting.objects.all()
output( qs.query )


# def q_get_compiler(obj, *args, **kwargs):
#     return 
qs = Meeting.objects.all()
qs.query = LoggingAg(qs.query)
output( list(qs) )
