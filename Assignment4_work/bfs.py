class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0

    def printq(self):
        "Print the content of queue"
        print self.list[::-1]

graph4 ={1:[7],
        2:[5],
        3:[1,2,5],
        4:[],
        5:[1,4,11],
        6:[],
        7:[],
        8:[7,10,11],
        9:[1,2,4,6,10],
        10:[5,6],
        11:[]
        }

class Solution:
    dist = []
    dist.append(99999)

    def BFS(self,graph,s):
        for i in range(1,12):
            self.dist.append(99999)

        self.dist[s] = 0
        Q = Queue()
        Q.push(s)

        while not Q.isEmpty():
            print "the present queue is "
            Q.printq()
            u = Q.pop()
            print "now exploring %d" %(u)
            for v in graph[u]:
                if self.dist[v] == 99999:
                    Q.push(v)
                    self.dist[v] = self.dist[u] + 1

a = Solution()
a.BFS(graph4,9)

