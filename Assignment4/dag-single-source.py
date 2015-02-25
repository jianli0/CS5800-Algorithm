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
        10:[]
        }


class Solution:
    def __init__(self):
        self.dist = []
        self.dist.append(float("inf"))
        self.prev = []
        self.prev.append(None)
        self.iteration = 1
        self.typo = [3, 9, 8, 5, 4, 6, 7, 2, 1, 10]

    def bellman(self,G,l,s):
        for u in G.keys():
            self.dist.append(float('inf'))
            self.prev.append(None)
        self.dist[s] = 0.0
        print "---iteration %d:---"%(self.iteration)
        #print "changset is %r"%(self.changeset)
        self.getdist()

        for u in self.typo:
            self.iteration += 1
            print "---iteration %d:---"%(self.iteration)
            for v in G[u]:
                    self.update(u,v,l)
                ###print "change set now is %r"%(self.changeset)
            self.getdist()

    def update(self,u,v,l):
        print " edge (%d,%d), length %.1f"%(u,v,l[(u,v)])####
        #print "dist[%d] = min(%d,%d)"%(v,self.dist[v],self.dist[u] + edgelength)###
        if self.dist[u]+ l[(u,v)]< self.dist[v]:
            self.dist[v] = self.dist[u]+ l[(u,v)]

    def getdist(self):
        for i in range(len(self.dist) -1):
            if self.dist[i+1] == 999:
                print "Node %d:INF"%(i+1)
            else:
                print "Node %d:%.1f"%(i+1,self.dist[i+1])

a = Solution()
a.bellman(graph,length,3)



