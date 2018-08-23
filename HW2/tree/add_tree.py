# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:02:24 2018

@author: yuan
"""

class Tree(object):
    def __init__(self, root):
       self.root = root
       
    def get_value_root(self):
       if self.root is not None:
           return self.root.value
       else:
           return None
       
    def printTree(self):
        root = self.root
        def get_level(node):
            if not node:
                return 0
            return 1 + max(get_level(node.right), get_level(node.left))
        m = get_level(root)
        n = 2**m - 1
        ans = [['|' for i in range(n)] for j in range(m)]
        def dfs(node = root, level = 0, pos = 0):
            if not node:
                return
            i = 2**(m - level - 1) - 1 + pos*(2**(m - level))
            ans[level][i] = str(node.val)
            dfs(node.left, level + 1, pos<<1)
            dfs(node.right, level + 1, (pos<<1) + 1)
        dfs()
        return ans


class Node(object):

   def __init__(self, value, left, right):
       self.value = value
       self.left = left
       self.right = right


if __name__ == '__main__':
   a = Node(2, None, None)
   b = Tree(a)
   print(b.get_value_root())