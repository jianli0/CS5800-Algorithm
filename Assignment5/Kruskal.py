length = {(1,5):5.4,
        (1,6):5.0,
        (1,8):5.4,
        (2,3):8.0,
        (2,4):7.5,
        (2,9):3.7,
        (3,4):3.5,
        (3,5):2.3,
        (3,7):6.8,
        (4,5):3.7,
        (4,6):2.8,
        (4,8):5.3,
        (5,6):6.5,
        (5,7):5.9,
        (5,9):4.9,
        (6,7):6.7,
        (6,9):4.8,
        (7,8):5.8
        }

graph ={1:[5,6,8],
    2:[3,4,9],
    3:[2,4,5,7],
    4:[2,3,5,6,8],
    5:[1,3,4,6,7,9],
    6:[1,4,5,7,9],
    7:[3,5,6,8],
    8:[1,4,7],
    9:[2,5,6]}

from collections import OrderedDict

class Solution:
    def __init__(self):
        self.X = []
        self.parent = []
        self.rank = []
        self.parent.append(None)
        self.rank.append(None)

    def kruskal(self,G,L):
        for i in G.keys():
            self.parent.append(None)
            self.rank.append(None)

        for u in G.keys():
            self.makeset(u)

        sorted_length = self.sortlength(L)
        for ((u,v),length) in sorted_length:
            print "--------------------------------"
            print "now exploring edge(%d,%d)"%(u,v)
            if not self.find(u) == self.find(v):
                self.X.append((u,v))
                self.union(u,v)
            print "the parent is %r"%(self.parent)
            print "MST now is %r"%(self.X)
            print "--------------------------------"

    def makeset(self,x):
        self.parent[x] = x
        self.rank[x] = 0

    def sortlength(self,L):
        return OrderedDict(sorted(L.items(),key = lambda x:x[1])).items()


    def find(self,x):
        if not x == self.parent[x]:
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

a = Solution()
a.kruskal(graph,length)

'''
(3 5) : 2.3
(4 6) : 2.8
(3 4) : 3.5
(2 9) : 3.7
(4 5) : 3.7
(6 9) : 4.8
(5 9) : 4.9
(1 6) : 5.0
(4 8) : 5.3
(1 5) : 5.4
(1 8) : 5.4
(7 8) : 5.8
(5 7) : 5.9
(5 6) : 6.5
(6 7) : 6.7
(3 7) : 6.8
(2 4) : 7.5
(2 3) : 8.0
'''






