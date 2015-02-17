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

        print "union %d to %d" %(y,x)
        self.parent[ry] = rx
        self.rank[rx] += 1

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

