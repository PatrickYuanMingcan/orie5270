# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 12:43:44 2018

@author: yuan
"""
from collections import defaultdict
from heapq import *
def find_shortest_path(name_txt_file, source, destination):
    
    #Load the data
    f = open(name_txt_file, "r")
    if f.mode == 'r':
        data = f.read()
    else:
        return
    
    #create graph
    #graph = {node1: dict1, node2: dict2, node3: dict3}
    #dict1 = {neighbor1: distance1, neighbor2: distance2}
    graph = defaultdict(list)
    data = data.split('\n')
    for i in range(len(data)//2):
        neighbor = data[2*i + 1].replace('(', '').replace(')', '').replace(',', ' ').split(' ')
        for j in range(len(neighbor)//2):
            graph[data[2*i]].append((int(neighbor[2*j + 1]),neighbor[2*j]))
    
    def dijkstra(graph, f, t):
        q, seen, mins = [(0,f,'')], set(), {f: 0}
        while q:
            (cost, v1, path) = heappop(q)
            if v1 not in seen:
                seen.add(v1)
                path = path + ',' + v1
                if v1 == t:
                    return cost, path
                for c, v2 in graph.get(v1, ()):
                    if v2 in seen:
                        continue
                    prev = mins.get(v2, None)
                    next = cost + c
                    if prev is None or next < prev:
                        mins[v2] = next
                        heappush(q, (next, v2, path))
        return float('inf')
    distance, path = dijkstra(graph, source, destination)
    path = path[1:].split(',')
    return (distance, path)