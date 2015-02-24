graph3 = {1 :[3,6],
    2 :[3,9],
    3 :[9],
    4 :[1,2,3,6,7,10],
    5 :[2,3,9],
    6 :[2,3,10],
    7 :[5,6,9,10],
    8 :[2,5,7,9,10],
    9 :[],
    10 : [2,3]}


class UF:
    def __init__(self):
        self.parent = []
        self.rank = []
        self.visited = []
        self.pre = []
        self.post = []
        self.clock = 1
        "initial"
        for i in range(0,11):
            self.parent.append(i)
            self.rank.append(0)
            self.visited.append(False)
            self.pre.append(None)
            self.post.append(None)


    def find(self,x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x
        '''
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        '''

    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        print "   %d parent is %d"%(x,rx)
        print "   %d parent is %d"%(y,ry)
        if rx == ry:
            print "   same root"
            return
        if self.rank[rx] > self.rank[ry]:
            print "   union second to first"
            self.parent[ry] = rx
        elif self.rank[rx] < self.rank[ry]:
            print "   union first to second"
            self.parent[rx] = ry
        elif self.rank[rx] == self.rank[ry]:
            print "   union second to first"
            self.parent[ry] = rx
            self.rank[rx] += 1
            print "   %d rank is now %d"%(rx,self.rank[rx])

    def DFS(self,graph,depth):
        for u in graph.keys():
            if not self.visited[u]:
                self.explore(graph,u,depth)

    def explore(self,graph,v,depth):
        self.visited[v] = True
        print "%d  visited[%d] sets True" %(depth,v)
        self.previsit(v)
        for u in graph[v]:
            if not self.visited[u]:
                print "   now union %d %d"%(u,v)
                self.union(v,u)
                print "   now exploring %d" %(u)
                self.explore(graph,u,depth + 1)
            else:
                print "   %d is already explored" %(v)
        self.postvisit(v)

    def previsit(self,v):
        self.pre[v] = self.clock
        print "   pre[%d] sets %d" %(v, self.clock)
        self.clock += 1

    def postvisit(self,v):
        self.post[v] = self.clock
        print "   post[%d] sets %d" %(v, self.clock)
        self.clock += 1

    def getparent(self):
        print "parent list is %r"%(self.parent[1:11])

    def getrank(self):
        print "rank list is %r"%(self.rank[1:11])


a = UF()
a.DFS(graph3,1)
a.getparent()
a.getrank()


