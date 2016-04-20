#!/usr/bin/env python3

'''
ftpsync.py -- transfer local files to FTP server

DO NOT USE -- use lftp command instead, start with 'cd /django-queryset ; mirror -v --reverse -X project --ignore-time --use-cache -X *.pickle -X *.doctree --dry-run'

'''
# "git ls-tree" from http://stackoverflow.com/questions/1910783/git-1-list-all-files-in-a-branch-2-compare-files-from-different-branch

import itertools, os, subprocess, sys
import ftplib
from ftplib import FTP


def find_files(topdir):
    for dirname, _, filenames in os.walk(topdir):
        for filename in filenames:
            yield os.path.join(dirname, filename)

# list files known to Git
paths = subprocess.check_output(
    'git ls-tree -r --name-only HEAD'.split()
    ).decode("utf-8").split('\n')

# zap Django site
paths = filter(
    lambda path: not path.startswith('project/'),
    paths)

# add slides
paths = itertools.chain(paths, find_files('_build'))
paths = list(paths)

for path in paths:
    print(path)

if 0:
    sys.exit(0)

print('Transferring {} files'.format(len(paths)))

try:
    user,pw = os.environ['FTP_AUTH'].split(':')
except KeyError:
    sys.exit('usage: FTP_AUTH=(user):(pass) ftpsync.py')

ftp = FTP(host='ftp.ipage.com', user=user, passwd=pw)
if 0:
    ftp.set_debuglevel(1)
try:
    ftp.cwd('django-queryset')

    path = None
    for num,path in enumerate(paths):
        print('{:3d}/{:3d} {}'.format(
            num+1, len(paths), path,
            ))

        if not path:
            print('??')
            continue

        if '/' in path:
            mydir = os.path.dirname(path)
            print('\t- mkdir {}'.format(mydir))
            # ignore '550 (mydir) File exists'
            try:
                ftp.mkd( mydir )
            except ftplib.error_perm:
                pass
            # except ftplib.all_errors:
            #     pass

        ftp.storbinary(
            'STOR {}'.format(path),
            open(path, 'rb')
        )
except Exception as exc:
    sys.exit('UHOH: {} path={}'.format(exc, path))
finally:
    ftp.quit()                  
