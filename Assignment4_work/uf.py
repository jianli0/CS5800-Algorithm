graph = {1 :[],
    2 :[8],
    3 :[8],
    4 :[2,6],
    5 :[2,7],
    6 :[2],
    7 :[1,6],
    8 :[1],
    9 :[3],}

class UF:
    def __init__(self):
        self.parent = []
        self.rank = []
        "initial"
        for i in range(0,11):
            self.parent.append(i)
            self.rank.append(0)


    def find(self,x):
        while self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        if self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[rx] = ry
            if self.rank[rx] == self.rank[ry]:
                self.rank[ry] += 1

    def startunion(self,graph):
        for u in graph.keys():
            for v in graph[u]:
                self.union(u,v)

    def getparent(self):
        print "parent list is %r"%(parent)

    def getrank(self):
        print "rank list is %r"%(rank)


a = UF()
a.startunion(graph)
a.getparent()
a.getrank()


