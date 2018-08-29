# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 12:15:32 2018

@author: yuan
"""

from pyspark import SparkConf, SparkContext
import sys
import numpy as np

def kmeans(data_file_name, cs_file_name):
	MAX_ITER = 100
	conf = SparkConf()
	sc = SparkContext(conf = conf)

	data = sc.textFile(data_file_name).map(lambda x: np.array([float(i) for i in x.split(' ')])).cache()
	cs = np.array(sc.textFile(cs_file_name).map(lambda x: np.array([float(i) for i in x.split(' ')])).collect())

	for _ in range(MAX_ITER):
		temp_data = data.map(lambda x: (np.argmin([np.linalg.norm(x - s) for s in cs]), (x, 1)))
		temp_cs = temp_data.reduceByKey(lambda x1, x2: (x1[0] + x2[0], x1[1] + x2[1])).sortByKey()
		cs = np.array(temp_cs.map(lambda x: x[1][0]/x[1][1]))
	
	f = open('output.txt', 'w')
	for x in cs:
		temp = ''
		for i in range(len(x) - 1):
			temp += str(x[i]) + " " 
		temp + '\n'
		f.write(temp)
	f.cloes()