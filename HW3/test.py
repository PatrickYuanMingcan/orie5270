# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 21:09:43 2018

@author: yuan
"""

import unittest
from FindNegativeCycle import find_negative_cycle
from FindShortestPath import find_shortest_path

class TestTree(unittest.TestCase):
    
    def test1(self):
        assert find_negative_cycle(testcase1) == ['8', '5', '7']
        
    def test2(self):
        assert find_shortest_path(testcase2, '2', '5') == (8, ['2', '5'])