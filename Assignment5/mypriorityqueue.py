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

    def allpop(self):
        return heapq.heappop(self.heap)

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
                print "Node%r.dist = INF"%(node)
            else:
                print "Node%r.dist = %r"%(node,dis)



