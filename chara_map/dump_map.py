#!python
# -*- mode: python; Encoding: utf-8; coding: utf-8 -*-
# Last updated: <2019/05/26 02:12:00 +0900>
"""
Dump chara code map.

Windows10 x64 + Python 2.7.16 32bit
"""

import os
import sys
import codecs

infile = "chara_conv_map.txt"


def main():
    if not os.path.exists(infile):
        print("Not found %s" % infile)
        sys.exit(1)

    with codecs.open(infile, 'r', 'utf-8') as f:
        lines = f.read()

    cnum = 0
    for i, s in enumerate(lines.splitlines()):
        if len(s) != 16:
            print("over 16 length. line %d" % i)
        for i in range(16):
            c = ord(s[i])
            if cnum == 0x20 or c != 0x0020:
                print("0x%04x,0x%04x" % (cnum, c))
            cnum += 1


if __name__ == '__main__':
    main()
