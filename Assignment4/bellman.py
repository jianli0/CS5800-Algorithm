length = {(1,3):4,
        (1,4):10,
        (1,5):9,
        (2,6):2,
        (2,7):2,
        (3,7):5,
        (3,8):8,
        (4,5):3,
        (4,9):-1,
        (6,7):4,
        (6,9):-1,
        (7,4):5,
        (7,5):6,
        (7,6):3,
        (8,9):5,
        (8,10):4,
        (9,8):5,
        (10,4):7,
        (10,6):4,
        (10,8):5
    }

graph ={1:[3,4,5],
        2:[6,7],
        3:[7,8],
        4:[5,9],
        5:[],
        6:[7,9],
        7:[4,5,6],
        8:[9,10],
        9:[8],
        10:[4,6,8]
        }

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



