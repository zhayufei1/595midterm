# reference https://neo4j.com/blog/accelerating-towards-natural-language-search-graphs/
import glob
import csv
from py2neo import *

graph = Graph(host='localhost', user='neo4j', password='password')
tx = graph.begin()

with open('c:\\Users\\sam.tsuei\\luckin\\a.txt','r') as f:
    file_contents = f.read()
    Nodes = Node("Artical", Text=str(file_contents))
    graph.create(Nodes)
    tx.merge(Nodes)