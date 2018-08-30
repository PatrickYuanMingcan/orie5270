# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:44:35 2018

@author: yuan
"""


import sys 
from pyspark import SparkConf, SparkContext
import numpy as np

#Load data
conf = SparkConf()
sc = SparkContext(conf = conf)
A = sc.textFile('A.txt').map(lambda x: [float(i) for i in x.split(',')])
v = sc.textFile('v.txt').map(lambda x: x.split(','))

#Calculation
A = A.zipWithIndex()
A = A.map(lambda x: (x[1], [(i, x[0][i]) for i in range(len(x[0]))]))
A = A.flatMapValues(lambda x: x)
A = A.map(lambda x: (x[1][0], (x[0], x[1][1])))
v = v.flatMap(lambda x: [(i, float(x[i])) for i in range(len(x))])

output = A.join(v)
output = output.map(lambda x: (x[1][0][0], x[1][0][1]*x[1][1]))
output = output.reduceByKey(lambda x1, x2: x1 + x2)

print(output.collect())