length = {(1,10):-9.2,
        (2,10):-2.0,
        (3,1):-4.2,
        (3,2):3.0,
        (3,4):9.3,
        (3,7):14.4,
        (3,9):18.7,
        (3,10):5.2,
        (4,2):11.4,
        (4,6):3.5,
        (5,2):-0.7,
        (5,7):-3.6,
        (5,10):4.2,
        (6,7):1.2,
        (6,10):-3.6,
        (7,10):-5.1,
        (8,1):-1.0,
        (8,10):-4.5,
        (9,5):17.5,
        (9,8):19.8
    }

graph ={1:[10],
        2:[10],
        3:[1,2,4,7,9,10],
        4:[2,6],
        5:[2,7,10],
        6:[7,10],
        7:[10],
        8:[1,10],
        9:[5,8],
        }

typo =[]

class Solution:
    def __init__(self):
        self.dist = []
        self.dist.append(999)
        self.prev = []
        self.prev.append(None)
        self.iteration = 1
        self.changeset = []

    def bellman(self,G,l,s):
        for u in G.keys():
            self.dist.append(999)
            self.prev.append(None)
        self.dist[s] = 0
        self.changeset.append(s)
        print "---iteration %d:---"%(self.iteration)
        #print "changset is %r"%(self.changeset)
        self.getdist()


        for i in range(len(G.keys()) - 1):
            self.iteration += 1
            print "---iteration %d:---"%(self.iteration)
            self.nowchangenode = self.changeset
            #print "now change node is %r"%(self.nowchangenode)
            self.changeset = []

            if self.nowchangenode:
                for (u,v) in l.keys():
                    if u in self.nowchangenode:
                        self.update(u,v,l[(u,v)])
                self.nowchangenode = []
                ###print "change set now is %r"%(self.changeset)
                self.getdist()

    def update(self,u,v,edgelength):
        #print "now edge is (%d,%d)"%(u,v)####
        #print "dist[%d] = min(%d,%d)"%(v,self.dist[v],self.dist[u] + edgelength)###
        if self.dist[u]+edgelength < self.dist[v]:
            self.dist[v] = self.dist[u]+edgelength
            self.changeset.append(v)

    def getdist(self):
        for i in range(len(self.dist) -1):
            if self.dist[i+1] == 999:
                print "Node %d:INF"%(i+1)
            else:
                print "Node %d:%d"%(i+1,self.dist[i+1])

a = Solution()
a.bellman(graph,length,3)



