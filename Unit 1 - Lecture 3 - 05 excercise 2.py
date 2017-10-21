# -*- coding: utf-8 -*-
"""
Created on ###### Sat Oct 21 19:22:58 CST 2017

@author: amblizer
"""
# Node is basically the same as "object", but is useful for later revise
class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

class Digraph(object):
    """edges is a dict mapping each node to a list of
    its children"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        # append dest to the value of key src
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                + dest.getName() + '\n'
            # ommit final empty line
        return result[:-1]

 # Graph iherit all tribute of Digraph, and make substitute
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

# build graph nodes and edges in excersice 2
def buildCityGraph():
    # add nodes
    nodes = []
    nodes.append(Node("ABC")) # nodes[0]
    nodes.append(Node("ACB")) # nodes[1]
    nodes.append(Node("BAC")) # nodes[2]
    nodes.append(Node("BCA")) # nodes[3]
    nodes.append(Node("CAB")) # nodes[4]
    nodes.append(Node("CBA")) # nodes[5]

    # build graph forward and backward
    g = Graph()
    for n in nodes:
        g.addNode(n)
    
    # add edges
    g.addEdge(Edge(g.getNode('ABC'),g.getNode('BAC')))
    g.addEdge(Edge(g.getNode('ABC'),g.getNode('ACB')))
    g.addEdge(Edge(g.getNode('BCA'),g.getNode('CBA')))
    g.addEdge(Edge(g.getNode('BCA'),g.getNode('BAC')))
    g.addEdge(Edge(g.getNode('CAB'),g.getNode('ACB')))
    g.addEdge(Edge(g.getNode('CAB'),g.getNode('CBA')))

    return g

print(buildCityGraph())