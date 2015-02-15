graph = {1 :[],
    2 :[8],
    3 :[8],
    4 :[2,6],
    5 :[2,7],
    6 :[2],
    7 :[1,6],
    8 :[1],
    9 :[3],}

edges = [(5,7),
        (4,2),
        (4,6),
        (6,2),
        (8,1),
        (7,1),
        (2,8),
        (7,6),
        (9,3),
        (5,2),
        (3,8)]

class UF:
    def __init__(self):
        self.parent = []
        self.rank = []
        "initial"
        for i in range(0,11):
            self.parent.append(i)
            self.rank.append(0)


    def find(self,x):
        '''
        while self.parent[x] != x:
            x = self.parent[x]
        return x
        '''
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        print "now union %d and %d" %(x,y)
        print "%d parent is %d"%(x,rx)
        print "%d parent is %d"%(y,ry)
        if rx == ry:
            print "same root"
            return
        if self.rank[rx] > self.rank[ry]:
            print "union second to first"
            self.parent[ry] = rx
        elif self.rank[rx] < self.rank[ry]:
            print "union first to second"
            self.parent[rx] = ry
        elif self.rank[rx] == self.rank[ry]:
            print "union second to first"
            self.parent[ry] = rx
            self.rank[rx] += 1
            print "%d rank is now %d"%(rx,self.rank[rx])

    def startunion(self,edges):
        for (u,v) in edges:
                self.union(u,v)

    def getparent(self):
        print "parent list is %r"%(self.parent[1:10])

    def getrank(self):
        print "rank list is %r"%(self.rank[1:10])


a = UF()
a.startunion(edges)
a.getparent()
a.getrank()


