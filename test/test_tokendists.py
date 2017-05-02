#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Pablo'
import nltk
import math
from nltk.tokenize import word_tokenize
from nltk import *
import unittest
from stringdists import Stringdists

class Teststringdists(unittest.TestCase):
    def test_vector(self):
        s=Stringdists()
        self.failUnlessEqual(s.binary_distance("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),0.0)
        self.failUnlessEqual(s.jaccard("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),0.6)
        self.failUnlessEqual(s.euclidean("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),1.0)
        self.failUnlessEqual(s.overlap("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),0.75)
        self.failUnlessEqual(s.manhattan("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),1.0)
        self.failUnlessEqual(s.matching_coefficient("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'), 0.75)
        self.failUnlessEqual(s.dice_coefficient("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),0.6)
        self.failUnlessEqual(s.cos("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),0.75)
        self.failUnlessEqual(s.masi_distance("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),0.802)
        self.failUnlessEqual(s.jaccard_ulacia("my house is pretty","the house my is pretty",'english'),1.0)
    def test_doc(self):
        s=Stringdists()
        self.failUnlessEqual(s.binary_distance(None,None,'c.txt','d.txt','english'),0.0)
        self.failUnlessEqual(s.jaccard(None,None,'c.txt','d.txt','english'),0.6)
        self.failUnlessEqual(s.euclidean(None,None,'c.txt','d.txt','english'),1.0)
        self.failUnlessEqual(s.overlap(None,None,'c.txt','d.txt','english'),0.75)
        self.failUnlessEqual(s.manhattan(None,None,'c.txt','d.txt','english'),1.0)
        self.failUnlessEqual(s.matching_coefficient(None,None,'c.txt','d.txt','english'),0.75)
        self.failUnlessEqual(s.dice_coefficient(None,None,'c.txt','d.txt','english'),0.6)
        self.failUnlessEqual(s.cos(None,None,'c.txt','d.txt','english'),0.75)
        self.failUnlessEqual(s.masi_distance(None,None,'c.txt','d.txt','english'),0.802)
        self.failUnlessEqual(s.jaccard_ulacia(None,None,'jaccard_modificado1.txt','jaccard_modificado2.txt','english'),1.0)

    def test_spellcheck_paraprhase(self):
        s=Stringdists()
        """ejemplo de como escribir el paraphrase_example.txt
        el niño come pescado, el muchacho de Maria engullo el peje velozmente,0.09090909090909091
        """
        with open('paraphrase_examples_jaccard.txt') as f:
            for line in f:
                data = line.split(',')
                self.failUnlessEqual(s.jaccard(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
        with open('paraphrase_examples_binary_distance.txt') as f:
            for line in f:
                data = line.split(',')
                self.failUnlessEqual(s.binary_distance(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
        with open('paraphrase_examples_euclidean.txt') as f:
            for line in f:
                data = line.split(',')
                self.failUnlessEqual(s.euclidean(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
        with open('paraphrase_examples_overlap.txt') as f:
            for line in f:
                data = line.split(',')
                self.failUnlessEqual(s.overlap(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
        with open('paraphrase_examples_manhattan.txt') as f:
            for line in f:
                data = line.split(',')
                self.failUnlessEqual(s.manhattan(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
        with open('paraphrase_examples_matching_coefficient.txt') as f:
            for line in f:
                data = line.split(',')
                self.failUnlessEqual(s.matching_coefficient(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
        with open('paraphrase_examples_dice_coefficient.txt') as f:
            for line in f:
                data = line.split(',')
                self.failUnlessEqual(s.dice_coefficient(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
        with open('paraphrase_examples_cos.txt') as f:
            for line in f:
                data = line.split(',')
                self.failUnlessEqual(s.cos(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
        with open('paraphrase_examples_masi_distance.txt') as f:
            for line in f:
                data = line.split(',')
                self.failUnlessEqual(s.masi_distance(data[0],data[1],None,None,'spanish'),float(data[2].strip()))

if __name__ == '__main__':
    unittest.main()