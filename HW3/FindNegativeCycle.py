# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 11:42:50 2018

@author: yuan
"""

def find_negative_cycle(name_txt_file):
    
    #Load the data
    f = open(name_txt_file, "r")
    if f.mode == 'r':
        data = f.read()
    else:
        return
    
    #create graph
    #graph = {node1: dict1, node2: dict2, node3: dict3}
    #dict1 = {neighbor1: distance1, neighbor2: distance2}
    graph = {}
    data = data.split('\n')
    for i in range(len(data)//2):
        temp = {}
        neighbor = data[2*i + 1].replace('(', '').replace(')', '').replace(',', ' ').split(' ')
        for j in range(len(neighbor)//2):
            temp[neighbor[2*j]] = int(neighbor[2*j + 1])
            #create node in graph if not have neighbor
            if neighbor[2*j] not in graph.keys():
                graph[neighbor[2*j]] = {}
        graph[data[2*i]] = temp
        
    #bellman_ford
    def bellman_ford(graph):
        #destination
        d = {} 
        #predecessor
        p = {}
        for node in graph:
            d[node] = float('inf')
            p[node] = None
        #set the graph start from data[1]
        d[data[0]] = 0
        for i in range(len(graph)):
            for u in graph:
                for v in graph[u]:
                    if d[v] > d[u] + graph[u][v]:
                        d[v] = d[u] + graph[u][v]
                        p[v] = u
        
        #check for negative cycle
        cycle = []
        for u in graph:
            for v in graph[u]:
                if d[v] > d[u] + graph[u][v]:
                    for i in range(len(graph)):
                        if v in cycle:
                            for j in range(len(cycle)):
                                if cycle[j] == v:
                                    return cycle[j:]
                        cycle.append(v)
                        v = p[v]
        return []
    
    cycle = bellman_ford(graph)[::-1]
    return cycle
    
    