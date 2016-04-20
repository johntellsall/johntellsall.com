#!/usr/bin/env python

'''
mimport.py -- import Meetup events

Export data with "Export to / Outlook Calendar"

USAGE:
	mimport.py going
'''

import datetime, fileinput, os, re, sys, warnings

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings.local'
sys.path.append('project/project')

from meetup.models import Meeting


def parse_keyvalue(lines):
    keyval_pat = re.compile('^([A-Z]\S+?)[:=]([^\r]*)')

    event = {}
    for key,value in ( 
            m.groups()
            for m in (keyval_pat.match(line)
                      for line in lines)
            if m
    ):
        if 0:
            print '\t',key,value
        event[key] = value
        if key == 'SUMMARY':
            yield event


def parse_events(lines):
    for event in parse_keyvalue( lines ):
        tstamp_str = event['DTSTART;TZID'].split(':')[-1]
        tstamp = datetime.datetime.strptime(
            tstamp_str.split('T')[0], # XX only date
            '%Y%m%d',
            )
        yield tstamp, event['SUMMARY']


def main():
    Meeting.objects.all().delete()
    for tstamp,name in parse_events( fileinput.input() ):
        print tstamp,name

        # TODO: use real UTC dates
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            Meeting(name=name, meet_date=tstamp).save()


if __name__=='__main__':
    main()
