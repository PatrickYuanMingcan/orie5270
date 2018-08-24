# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:07:34 2018
@author: yuan
"""
import unittest
from tree.add_tree import Tree


class TestTree(unittest.TestCase):
    def test1(self):
        t = Tree(1)
        assert t.printTree() == [['1']]

    def test2(self):
        t = Tree(1)
        t.left = Tree(2)
        t.right = Tree(3)
        t.left.left = Tree(4)
        assert t.printTree() == [['|', '|', '|', '1', '|', '|', '|'],
                                 ['|', '2', '|', '|', '|', '3', '|'],
                                 ['4', '|', '|', '|', '|', '|', '|']]

    def test3(self):
        t = Tree(1)
        t.left = Tree(2)
        t.right = Tree(3)
        t.left.left = Tree(4)
        t.left.right = Tree(5)
        t.right.left = Tree(6)
        t.right.right = Tree(7)
        assert t.printTree() == [['|', '|', '|', '1', '|', '|', '|'],
                                 ['|', '2', '|', '|', '|', '3', '|'],
                                 ['4', '|', '5', '|', '6', '|', '7']]
