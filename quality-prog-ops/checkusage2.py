#!/usr/bin/env python

import subprocess

def main():
    ps_text = subprocess.check_output(
        'ps -e -o pcpu,rss,comm --no-headers --sort=-pcpu | head',
        shell=True)
    ps_text = ps_text.decode()
    print(ps_text)
    ps_lines = ps_text.split('\n')
    print(ps_lines)
    for line in ps_lines:
        if not line:
            continue
        pcpu, rss, command = line.split(None, 2)
        usage = int(float(pcpu) * int(rss) / 100.)
        print(usage, command)

if __name__=='__main__':
    main()
