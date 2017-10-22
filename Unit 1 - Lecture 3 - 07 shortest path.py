# -*- coding: utf-8 -*-
"""
Created on ###### Sun Oct 22 11:01:20 CST 2017

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


# use graphtype chosing graph or diagraph
def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

# print format
def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += ' -> '
    return result

# depth first, left first search
def DFS(graph, start, end, path, shortest, toPrint = False):
    """
    graph: digraph
    start, end: nodes
    path, shortest: lists of nodes
    return: shortest path from start to end, if exist
    """
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        # avoid cycles
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newpath = DFS(graph, node, end, path, shortest, toPrint)
                if newpath != None:
                    shortest = newpath
        elif toPrint:
            print('Already visited:', node)
    return shortest

# def shortestPath(graph, start, end, toPrint = False):
#     """
#     Same as DFS
#     """
#     return DFS(graph, start, end, [], None, toPrint)


# Breadth-first Search (BFS)
def BFS(graph, start, end, toPrint = False):
    """
    graph: digraph
    start, end: nodes
    path, shortest: lists of nodes
    return: shortest path from start to end, if exist
    """
    initPath = [start]
    # store paths to be explored
    pathQueue = [initPath]
    if toPrint:
        print('Current BFS path:', printPath(pathQueue))
    while len(pathQueue) != 0:
        # get and remove first-left(oldest) element in pathQueue
        tmpPath = pathQueue.pop(0)
        print('Current BFS path:', printPath(tmpPath))
        # if last node is end, right path is found
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        # if not found, extend pathQueue by childrenof(lastNode)
        for nextNode in graph.childrenOf(lastNode):
            # avoiding duplicates
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None

# test BFS
def shortestPath(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return BFS(graph, start, end, toPrint)

# build digraph and test
def testSP(src, dest):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(src), g.getNode(dest), toPrint = True)

testSP('Boston', 'Denver')