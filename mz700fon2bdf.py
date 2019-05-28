#!python
# -*- mode: python; Encoding: utf-8; coding: utf-8 -*-
# Last updated: <2019/05/25 22:38:43 +0900>
"""
Convert 8x8 dot bitmap font image to BDF.

* Windows10 x64 + Python 2.7.16 32bit
"""

import argparse
import csv
import os
import sys
from PIL import Image


def get_chara_pat(im, bx, by, w, h, bgcol):
    """Get 1 character bit pattern data."""
    d = []
    for y in range(h):
        pat = 0
        addbit = 0x80
        for x in range(w):
            if addbit == 0:
                pat <<= 8
                addbit = 0x80
            c = im.getpixel((bx + x, by + y))
            if c != bgcol:
                pat |= addbit
            addbit >>= 1
        d.append(pat)
    return d


def get_chara_bdf(lst, cnum, w):
    """Get 1 character BDF text."""
    d = []
    d.append("STARTCHAR %02x" % cnum)
    d.append("ENCODING %d" % cnum)
    d.append("SWIDTH 960 0")
    d.append("DWIDTH %d 0" % w)
    d.append("BBX %d %d 0 0" % (w, w))
    d.append("BITMAP")
    s = "%x"
    if w <= 8:
        s = "%02x"
    elif w <= 16:
        s = "%04x"
    elif w <= 24:
        s = "%06x"
    elif w <= 32:
        s = "%08x"
    for v in lst:
        d.append(s % v)

    d.append("ENDCHAR")
    return '\n'.join(d)


def dump_header(header, cnum, defchar):
    """Dump BDF header."""
    if not os.path.exists(header):
        print("Not found %s" % header)
        sys.exit(1)

    # read header text file
    with open(header, 'r') as f:
        data = f.read()

    for s in data.splitlines():
        if s.find('DEFAULT_CHAR') == 0:
            print("DEFAULT_CHAR %d" % defchar)
        else:
            print(s)

    print("CHARS %d" % cnum)


def dump_footer():
    """Dump BDF footer."""
    print("ENDFONT")


def get_convlist(convlist):
    """Get character code convert list."""
    if convlist is None:
        return None

    if not os.path.exists(convlist):
        print("Not found %s" % convlist)
        sys.exit(1)

    d = {}
    with open(convlist, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            k = int(row[0], 0)
            v = int(row[1], 0)
            d[k] = v

    return d


def conv_bdf(path, header, startcode, endcode, setcode, defchar, convlist):
    """Convert image to BDF."""
    if not os.path.exists(path):
        print("Not found %s" % path)
        sys.exit(1)

    imorig = Image.open(path)
    im = imorig.convert("RGB")
    w = im.width / 16
    xcount = im.width / w
    ycount = im.height / w

    if startcode is None:
        startcode = 0x00
    if endcode is None:
        endcode = xcount * ycount - 1
    if setcode is None:
        setcode = 0x00
    if defchar is None:
        defchar = 0x20

    convdic = get_convlist(convlist)

    chara_data = {}
    bgcol = im.getpixel((0, 0))
    cnt = 0
    for iy in range(ycount):
        for ix in range(xcount):
            if startcode <= cnt and cnt <= endcode:
                lsetcode = setcode
                if convdic is not None and cnt in convdic:
                    lsetcode = convdic[cnt]
                d = get_chara_pat(im, ix * w, iy * w, w, w, bgcol)
                if lsetcode == defchar or sum(d) != 0:
                    chara_data[lsetcode] = get_chara_bdf(d, lsetcode, w)
            cnt += 1
            setcode += 1

    dump_header(header, len(chara_data), defchar)
    for key in sorted(chara_data.keys()):
        print(chara_data[key])
    dump_footer()


def main():
    """Parse args and call main."""
    p = argparse.ArgumentParser(description="Convert image to BDF.")
    p.add_argument("--version", action='version', version='%(prog)s 1.0.0')
    p.add_argument("infile", help="Image file.")
    p.add_argument("header", help="BDF header text file.")
    p.add_argument("--start", type=int, help="start code number")
    p.add_argument("--end", type=int, help="end code number")
    p.add_argument("--setcode", type=int, help="set first code")
    p.add_argument("--defchar", type=int, help="default char code")
    p.add_argument("--convlist", help="chara number convert list")
    args = p.parse_args()

    infile = args.infile
    header = args.header
    startcode = args.start
    endcode = args.end
    setcode = args.setcode
    defchar = args.defchar
    convlist = args.convlist

    conv_bdf(infile, header, startcode, endcode, setcode, defchar, convlist)


if __name__ == '__main__':
    main()
