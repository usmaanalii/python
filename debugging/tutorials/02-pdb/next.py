# next.py

# !/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#

import pdb


def calc(i, n):
    j = i * n
    return j


def f(n):
    for i in range(n):
        j = calc(i, n)
        print(i, j)
    return


if __name__ == '__main__':
    pdb.set_trace()
    f(5)

# next -> Does not enter functions called from the statement being executed
#         It steps all the way through the function call to the next statement
#         in the current function

# until -> lets you skip to the next line (or given line) allows
#          skipping over long blocks by executing all that happens between