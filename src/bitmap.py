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
"""

import array


class BitMap(object):
    """
    BitMap class
    """

    def __init__(self, maxnum):
        """
        Create a BitMap
        """
        self.bitmap = array.array('b', [0 for i in range(maxnum)])

    def __del__(self):
        """
        Destroy the BitMap
        """
        del self.bitmap

    def set(self, pos):
        """
        Set the value of bit@pos to 1
        """
        self.bitmap[pos] = 1

    def reset(self, pos):
        """
        Reset the value of bit@pos to 0
        """
        self.bitmap[pos] = 0

    def flip(self, pos):
        """
        Flip the value of bit@pos
        """
        self.bitmap[pos] = 1 - self.bitmap[pos]

    def count(self):
        """
        Count bits set
        """
        return sum(self.bitmap)

    def size(self):
        """
        Return size
        """
        return len(self.bitmap)

    def test(self, pos):
        """
        Return bit value
        """
        return self.bitmap[pos]

    def any(self, pos):
        """
        Test if any bit is set
        """
        return self.count() > 0

    def none(self, pos):
        """
        Test if no bit is set
        """
        return self.count() == 0

    def all(self, pos):
        """
        Test if all bits are set
        """
        return self.count() == self.size()
