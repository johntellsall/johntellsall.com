#!/usr/bin/env python

import glob, os

dull = '''
adlist ae_evport ae_kqueue bitops crc64 endianconv
dict intset lzf_c lzf_d rand pqsort redis-benchmark sds sort
t_hash t_list t_set t_string t_zset zipmap zmalloc
'''.split()

out = []

for path in sorted(glob.glob('redis*/src/*.c')):
    name = os.path.splitext(os.path.basename(path))[0]
    if name in dull:
        print '(dull: {})'.format(name)
        continue
    with open(path) as myfile:
        line = myfile.readline().rstrip()
        if len(line) < 10:
            line = myfile.readline().rstrip()
        print path, line
        out.append( '<a href="{}">{}</a> {} <br/>\n'.format(
            path, name, line
        ) )

with open('pview.html', 'w') as outf:
    outf.write( ''.join(out) )
