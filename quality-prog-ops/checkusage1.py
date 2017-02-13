#!/usr/bin/env python

import subprocess

def main():
    ps_text = subprocess.check_output(
        'ps -e -o pcpu,comm --sort=-pcpu | head'.split(), shell=True)
    print(ps_text.decode())

if __name__=='__main__':
    main()
