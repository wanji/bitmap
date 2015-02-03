#!/usr/bin/env python
# coding: utf-8

#########################################################################
#########################################################################

"""
   File Name: bitmap.py
      Author: Wan Ji
      E-mail: wanji@live.com
  Created on: Thu May  1 15:26:18 2014 CST
"""
DESCRIPTION = """
BitMap class
"""

import array


class BitMap(object):
    """
    BitMap class
    """

    BITMASK = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
    BIT_CNT = [bin(i).count("1") for i in xrange(256)]

    def __init__(self, maxnum=0):
        """
        Create a BitMap
        """
        nbytes = (maxnum + 7) / 8
        self.bitmap = array.array('B', [0 for i in range(nbytes)])

    def __del__(self):
        """
        Destroy the BitMap
        """
        pass

    def set(self, pos):
        """
        Set the value of bit@pos to 1
        """
        self.bitmap[pos / 8] |= self.BITMASK[pos % 8]

    def reset(self, pos):
        """
        Reset the value of bit@pos to 0
        """
        self.bitmap[pos / 8] &= ~self.BITMASK[pos % 8]

    def flip(self, pos):
        """
        Flip the value of bit@pos
        """
        self.bitmap[pos / 8] ^= self.BITMASK[pos % 8]

    def count(self):
        """
        Count bits set
        """
        return sum([self.BIT_CNT[x] for x in self.bitmap])

    def size(self):
        """
        Return size
        """
        return len(self.bitmap) * 8

    def test(self, pos):
        """
        Return bit value
        """
        return (self.bitmap[pos / 8] & self.BITMASK[pos % 8]) != 0

    def any(self):
        """
        Test if any bit is set
        """
        return self.count() > 0

    def none(self):
        """
        Test if no bit is set
        """
        return self.count() == 0

    def all(self):
        """
        Test if all bits are set
        """
        return (self.count() + 7) / 8 * 8 == self.size()

    def nonzero(self):
        """
        Get all non-zero bits
        """
        return [i for i in xrange(self.size()) if self.test(i)]

    def tostring(self):
        """
        Convert BitMap to string
        """
        return "".join([("%s" % bin(x)[2:]).zfill(8)
                        for x in self.bitmap[::-1]])

    @classmethod
    def fromstring(cls, bitstring):
        """
        Construct BitMap from string
        """
        nbits = len(bitstring)
        bm = BitMap(nbits)
        for i in xrange(nbits):
            if bitstring[-i-1] == '1':
                bm.set(i)
            elif bitstring[-i-1] != '0':
                raise Exception("Invalid bit string!")
        return bm
