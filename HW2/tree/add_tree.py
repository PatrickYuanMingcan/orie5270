# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:02:24 2018
@author: yuan
"""
class Tree(object):
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None    
    def printTree(self):
        def get_level(node):
            if not node:
                return 0
            return 1 + max(get_level(node.right), get_level(node.left))
        m = get_level(self)
        n = 2**m - 1
        ans = [['|' for i in range(n)] for j in range(m)]
        def dfs(node = self, level = 0, pos = 0):
            if not node:
                return
            i = 2**(m - level - 1) - 1 + pos*(2**(m - level))
            ans[level][i] = str(node.val)
            dfs(node.left, level + 1, pos<<1)
            dfs(node.right, level + 1, (pos<<1) + 1)
        dfs()
        return ans
if __name__ == '__main__':
   t = Tree(1)
   t.left = Tree(2)
   t.left.left = Tree(3)
   print(t.printTree())
