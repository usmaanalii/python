#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 09:15:27 2016

@author: usmaanali
"""


def gcd(m, n):
    while m % n != 0:  # whilst m is not divisible by n
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n


class Fraction:
    def __init__(self, top, bottom):

        # integer check
        if isinstance(top, int) and isinstance(bottom, int):
            common = gcd(top, bottom)
            self.num = top // common
            self.den = bottom // common

        else:
            raise RuntimeError("Integers only")

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

# Implement the simple methods getNum and getDen
# that will return the numerator and denominator of a fraction.
    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

# Implement __mul__
    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)

# Implement __truediv__
    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num

        return Fraction(newnum, newden)

# Implement __sub__
    def __sub__(self, other):
        newnum = (self.num * other.den) - (other.num * self.den)
        newden = self.den * other.den

        return Fraction(newnum, newden)

# Implement __lt__
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

# Implement __gt__
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

# Implement __le__
    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum

# Implement __ge__
    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum


x = Fraction(1, 2)
y = Fraction(2, 4)

print (x >= y)
