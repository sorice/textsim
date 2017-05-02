#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Pablo'

import unittest
import chardists
from chardists import Chardists

class Testchardists(unittest.TestCase):
    def test_vector(self):
        c=Chardists()
        self.failUnlessEqual(c.lcs("thisisatest","testing123testing"),"tsitest")
        self.failUnlessEqual(c.longlcs("thisisatest","testing123testing"),0.6363636363636364)
        self.failUnlessEqual(c.damerau_levenshtein_distance("jellyfish","smellyfishs"),0.7272727272727273)
           
    def test_doc(self):
        s=Chardists()
        self.failUnlessEqual(s.lcs(None,None,'chardists_lcs_a.txt','chardists_lcs_b.txt'),"tsitest")
        self.failUnlessEqual(s.longlcs(None,None,'chardists_lcs_a.txt','chardists_lcs_b.txt'),0.6363636363636364)
        self.failUnlessEqual(s.damerau_levenshtein_distance(None,None,'chardists_a.txt','chardists_b.txt'),0.7272727272727273)
if __name__ == '__main__':
    unittest.main()