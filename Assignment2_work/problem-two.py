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


graph2 = {1 : [3,4,10],
        2 : [8],
        3 : [4],
        4 : [],
        5 : [2,10],
        6 : [10],
        7 : [3,4,10],
        8 : [3],
        9 : [2,3,4,5,8],
        10 : [3,4,8]}

graph4= {1:[2,4],
        2:[7,8],
        3:[8],
        4:[7],
        5:[9,10],
        6:[2,8],
        7:[3,10],
        8:[7],
        9:[1],
        10:[3,6]
        }

class Solution:
# initial
    visited = []
    visited.append(False)

    pre = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pre.append(0)

    post = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    post.append(0)

    publicClock = 1

    def dfs(self,graph,depth):
        for i in graph.keys():
            self.visited.insert(i,False)
        for i in graph.keys():
            if not self.visited[i]:
                self.explore(graph,i,depth)

    def explore(self,graph,v,depth):
        print "now exploring %d" %(v)
        print "depth %d"%(depth)
        self.visited[v] = True
        print "visited[%d] sets True" %(v)
        self.previsit(v)
        for u in graph[v]:
            if not self.visited[u]:
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
        print self.pre[0:12]

    def getpost(self):
        print self.post[0:12]
'''
a1 = Solution()
a1.dfs(graph1,1)
a1.getpre()
a1.getpost()
'''

'''
a2 = Solution()
a2.dfs(graph2,1)
a2.getpre()
a2.getpost()
'''
a4 = Solution()
a4.dfs(graph4,1)
a4.getpre()
a4.getpost()

