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
            x = self.parent[x]
        return x

    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        print "now union %d and %d" %(x,y)
        if rx == ry:
            print "same root"
            return
        if self.rank[rx] > self.rank[ry]:
            print "union second to first"
            self.parent[ry] = rx
        else:
            print "union first to second"
            self.parent[rx] = ry
            if self.rank[rx] == self.rank[ry]:
                self.rank[ry] += 1
                print "%d rank is now %d"%(ry,self.rank[ry])

    def startunion(self,graph):
        for u in graph.keys():
            for v in graph[u]:
                self.union(u,v)

    def getparent(self):
        print "parent list is %r"%(self.parent)

    def getrank(self):
        print "rank list is %r"%(self.rank)


a = UF()
a.startunion(graph)
a.getparent()
a.getrank()


