graph1 = {1 : [4,5,6],
        2 : [3,4,7,9],
        3 : [2,10],
        4 : [1,2,6],
        5 : [1,7,9],
        6 : [1,4,8,9,10],
        7 : [2,5,8],
        8 : [6,7,9,10],
        9 : [2,5,6,8],
        10 : [3,6,8]}

graph11 ={1:[10],
        2:[10],
        3:[1,2,4,7,9,10],
        4:[2,6],
        5:[2,7,10],
        6:[7,10],
        7:[10],
        8:[1,10],
        9:[5,8],
        10:[]
        }



class Solution:
# initial
    visited = []
    visited.append(False)

    pre = []
    pre.append(0)

    post = []
    post.append(0)

    publicClock = 1

    def dfs(self,graph,depth):
        for i in graph.keys():
            self.visited.append(False)
            self.pre.append(0)
            self.post.append(0)

        for i in graph.keys():
            if not self.visited[i]:
                self.explore(graph,i,depth)

    def explore(self,graph,v,depth):
        self.visited[v] = True
        print "visited[%d] sets True" %(v)
        self.previsit(v)
        for u in graph[v]:
            if not self.visited[u]:
                print "now exploring %d" %(u)
                self.explore(graph,u,depth + 1)
            else:
                print "%d is already explored" %(v)
        self.postvisit(v)

    def previsit(self,v):
        self.pre[v] = self.publicClock
        print "pre[%d] sets %d" %(v, self.publicClock)
        print "clock increase from %d to %d"%(self.publicClock,self.publicClock + 1)
        self.publicClock += 1

    def postvisit(self,u):
        self.post[u] = self.publicClock
        print "post[%d] sets %d" %(u, self.publicClock)
        print "clock increase from %d to %d"%(self.publicClock,self.publicClock + 1)
        self.publicClock += 1

    def getpre(self):
        print self.pre[1:]

    def getpost(self):
        print self.post[1:]

a = Solution()
a.dfs(graph11,1)
a.getpre()
a.getpost()
