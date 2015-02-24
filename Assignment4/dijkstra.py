import heapq

length = {(1,2):3,
        (1,7):4,
        (2,3):4,
        (2,9):5,
        (3,10):1,
        (4,2):7,
        (6,4):9,
        (6,7):2,
        (6,9):4,
        (7,4):8,
        (7,6):9,
        (7,10):9,
        (8,6):3,
        (8,9):3,
        (8,10):8,
        (9,3):6,
        (9,7):10,
        (10,3):8,
        (10,4):9,
        (10,8):4
    }

graph ={1:[2,7],
        2:[3,9],
        3:[10],
        4:[2],
        5:[],
        6:[4,7,9],
        7:[4,6,10],
        8:[6,9,10],
        9:[3,7],
        10:[3,4,8]
        }

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
            if dis == 999:
                print "Node%d.dist = INF"%(node)
            else:
                print "Node%d.dist = %d"%(node,dis)



#test for heap class
'''
a = PriorityQueue()
a.push(1,4)
a.printHeap()
a.push(2,5)
a.push(3,6)
a.push(4,3)
a.printHeap()
a.decreasekey(2,1)
a.printHeap()
'''

class Solution:
    def __init__(self):
        self.dist = []
        self.dist.append(999)
        self.prev = []
        self.prev.append(None)
        self.heap = PriorityQueue()
        self.step = 1

    def dijkstra(self,G,l,s):
        for u in graph.keys():
            self.dist.append(999)
            self.prev.append(None)
        self.dist[s] = 0
        self.getdist()#####

        # makequeue
        for i in range(1,11):
            self.heap.push(i, self.dist[i])

        while not self.heap.isEmpty():
            print "---step %d---"%(self.step)
            self.step += 1
            self.getdist()
            self.heap.printHeap()
            u = self.heap.pop()
            for v in G[u]:
                if self.dist[v] > self.dist[u] + l[(u,v)]:
                    self.dist[v] = self.dist[u] + l[(u,v)]
                    self.prev[v] = u
                    self.heap.decreasekey(v,self.dist[v])


    def getdist(self):
        for i in range(1,11):
            if self.dist[i] == 999:
                print "%d: INF"%(i),
            else:
                print "%d : %d"%(i,self.dist[i]),
        print
        #print "dist is %r"%(self.dist[1:])

    def getprev(self):
        print self.prev[1:]


a = Solution()
a.dijkstra(graph,length,3)



