length = {(1,3):2,
    (1,4):7,
    (1,7):8,
    (2,3):10,
    (2,4):4,
    (2,5):8,
    (3,4):4,
    (3,6):1,
    (3,9):5,
    (4,5):5,
    (4,7):9,
    (4,9):2,
    (5,6):9,
    (5,8):5,
    (6,7):2,
    (6,8):3,
    (7,8):5,
    (7,9):5}

graph = {1:[3,4,7],
    2:[3,4,5],
    3:[1,2,4,6,9],
    4:[1,2,3,5,7,9],
    5:[2,4,6,8],
    6:[3,5,7,8],
    7:[1,4,6,8,9],
    8:[5,6,7],
    9:[3,4,7]}

import heapq
class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.

      Note that this PriorityQueue does not allow you to change the priority
      of an item.  However, you may insert the same item multiple times with
      different priorities.
    """
    def  __init__(self):
        self.heap = []

    def push(self, item, item_dist):
        # FIXME: restored old behaviour to check against old results better
        entry = [item_dist,item]
        heapq.heappush(self.heap, entry)

    def pop(self):
        [_, item] = heapq.heappop(self.heap)
        #  (_, item) = heapq.heappop(self.heap)
        return item

    def decreasekey(self, item, item_newdist):
        '''when a distance value decrease'''
        for [dis,it] in self.heap:
            if it == item:
                index = self.heap.index([dis,it])
                self.heap[index] = [item_newdist,it]
                heapq._siftdown(self.heap,0,index)

    def isEmpty(self):
        return len(self.heap) == 0

    def printHeap(self):
        print "Heap is "
        for [dis,node] in self.heap:
            print "%d.cost= %.1f"%(node,dis)


class Solution():
    def __init__(self,s):
        self.cost = []
        self.prev = []
        self.cost.append(float("inf"))
        self.prev.append(None)
        self.start = s
        self.heap = PriorityQueue()
        self.step = 1
        self.visited = []
        self.visited.append(False)

    def prim(self,G,L):
        '''initi'''
        for i in G.keys():
            self.cost.append(float("inf"))
            self.prev.append(None)
            self.visited.append(False)
        self.cost[self.start] = 0

        for i in range(1,10):
            self.heap.push(i,self.cost[i])

        while not self.heap.isEmpty():
            print "---step %d---"%(self.step)
            self.step += 1
            self.getcost()
            self.heap.printHeap()
            v = self.heap.pop()
            self.visited[v] = True
            self.printvisited()
            for z in G[v]:
                if self.visited[z] == False:
                    if (v,z) in length.keys():
                        if self.cost[z] > L[(v,z)]:
                            self.cost[z] = L[(v,z)]
                    elif (z,v) in length.keys():
                        if self.cost[z] > L[(z,v)]:
                            self.cost[z] = L[(z,v)]
                    self.prev[z] = v
                    self.heap.decreasekey(z,self.cost[z])

    def printvisited(self):
        for i in range(len(self.visited)-1):
            print "%d.visited = %r"%(i+1,self.visited[i+1])


    def getcost(self):
        print "cost is"
        for i in range(1,10):
            print "(%d : %.1f)"%(i,self.cost[i]),
        print
        #print "dist is %r"%(self.dist[1:])

    def getprev(self):
        print self.prev[1:]


a = Solution(5)
a.prim(graph,length)





