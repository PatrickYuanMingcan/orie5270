# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:07:34 2018

@author: yuan
"""

import unittest
from tree.add_tree import Tree
from tree.add_tree import Node

class TestTree(unittest.TestCase):
    
    def test1(self):
        t = Tree(Node(1, None, None))
        assert t.printTree() == [['1']]
        
    def test2(self):
        t = Tree(Node(1, None, None))
        t.left = Tree(Node(2, None, None))
        t.right = Tree(Node(3, None, None))
        t.left.left = Tree(Node(4, None, None))
        assert t.printTree() == [['|','|','|','1','|','|','|'],
                          ['|','2','|','|','|','3','|'],
                          ['4','|','|','|','|','|','|',]]
        
    def test3(self):
        t = Tree(Node(1, None, None))
        t.left = Tree(Node(2, None, None))
        t.left.left = Tree(Node(3, None, None))
        assert t.printTree() == [['|','|','|','1','|','|','|'],
                          ['|','2','|','|','|','|','|'],
                          ['3','|','|','|','|','|','|',]]
