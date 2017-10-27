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


class WeightedEdge(Edge):
    """
    Write a WeightedEdge class that extends Edge. Its constructor
    requires a weight parameter, as well as the parameters from
    Edge. You should additionally include a getWeight method. The
    of 3 should be "A->B (3)".
    string value of a WeightedEdge from node A to B with a weight
    """
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        # should be Edge.__str__(self) + " (" + str(self.weight) + ")"
        return self.src.getName() + '->' + self.dest.getName() + ' (' + self.getWeight() + ')'