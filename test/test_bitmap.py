#!/usr/bin/env python
# coding: utf-8

#########################################################################
#########################################################################

"""
   File Name: test_bitmap.py
      Author: Wan Ji
      E-mail: wanji@live.com
  Created on: Sun Jan 25 00:05:50 2015 CST
"""
DESCRIPTION = """
"""

import unittest
from bitmap import BitMap
try:
    from past.builtins import xrange
except ImportError:
    pass


class TestBitMap(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.v_str = [
            "00001111000011110000111100001111",
            "10101001000010101000001101010101",
            "00101000100101000010101100111101",
            "0000111101111000011110000",
            "1010100101101000001101010100000110101",
            "00101000110100001010110011",
            "11111111111111111111111111111111",
            "00000000000000000000000000000000",
            "111111111111111111111111111",
            "000000000000000000000000000"]

    @classmethod
    def tearDownClass(cls):
        pass

    def helper_str_zfill(self, bitstr):
        return bitstr.zfill((len(bitstr) + 7) // 8 * 8)

    def test_str(self):
        """ Test BitMap: create
        """
        for bitstr in self.v_str:
            bm = BitMap.fromstring(bitstr)
            self.assertEqual(self.helper_str_zfill(bitstr), bm.tostring())

    def test_count(self):
        """ Test BitMap: create
        """
        for bitstr in self.v_str:
            bm = BitMap.fromstring(bitstr)
            self.assertEqual(bitstr.count("1"), bm.count())
            self.assertEqual(bitstr.count("1"),
                             len([i for i in xrange(bm.size()) if bm.test(i)]))

        for bitstr in self.v_str[:-4]:
            self.assertTrue(BitMap.fromstring(bitstr).any())
        self.assertTrue(BitMap.fromstring(self.v_str[-2]).all())
        self.assertTrue(BitMap.fromstring(self.v_str[-1]).none())

    def test_op(self):
        """ Test BitMap: create
        """
        bitstr = "000000000000000000000000000000000"
        bitlst = list(bitstr)
        bm = BitMap.fromstring(bitstr)

        v_pos = [1, 2, 3, 5, 9]

        for i in v_pos:
            bm.set(i)
            bitlst[-i-1] = '1'
        self.assertEqual(self.helper_str_zfill("".join(bitlst)),
                         bm.tostring())
        self.assertEqual(bm.count(), len(v_pos))

        for i in v_pos:
            bm.reset(i)
            bitlst[-i-1] = '0'
        self.assertEqual(self.helper_str_zfill("".join(bitlst)),
                         bm.tostring())
        self.assertEqual(self.helper_str_zfill(bitstr),
                         bm.tostring())
        self.assertEqual(bm.count(), 0)

        for i in v_pos:
            bm.flip(i)
            bitlst[-i-1] = '1'
        self.assertEqual(self.helper_str_zfill("".join(bitlst)),
                         bm.tostring())
        self.assertEqual(bm.count(), len(v_pos))


if __name__ == '__main__':
    unittest.main(failfast=True)
    # cProfile.run('unittest.main(failfast=True)')
