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

graph1 ={1:[5,8],
        2:[4,6,7],
        3:[4,6,7,8],
        4:[3,5,7,8],
        5:[3,6],
        6:[3,4,5,8],
        7:[2],
        8:[3,4,5,6]
        }

graph2 ={1:[5,8],
        2:[4,6,7],
        3:[4,6,7,8],
        4:[3,5,7,8],
        5:[3,6],
        6:[3,4,5,8],
        7:[2,3],
        8:[4,5,6]
        }
graph3 ={1:[5,8],
        2:[4,6,7],
        3:[4,6,7,8],
        4:[3,5,7,8],
        5:[3,6],
        6:[3,4,5,8],
        7:[2,3,4],
        8:[5,6]
        }

graph4 ={1:[5,8],
        2:[4,6,7],
        3:[4,5,6,8],
        4:[3,5,7,8],
        5:[3,6,8],
        6:[3,4,5,8],
        7:[2,3,4],
        8:[5,6]
        }

graph5 ={1:[5,8],
        2:[4,6,7],
        3:[4,5,6,8],
        4:[3,5,6,7,8],
        5:[3,6,8],
        6:[3,5,8],
        7:[2,3,4],
        8:[5,6]
        }

graph6 ={1:[5,8],
        2:[4,6,7],
        3:[5,6,8],
        4:[3,5,6,7,8],
        5:[3,6,8],
        6:[3,5,8],
        7:[2,3,4],
        8:[5]
        }

class Solution:
    def __init__(self,graph):
        self.graph = graph
        self.visited = []
        self.parent = {}
        for i in self.graph.keys():
            self.visited.append(False)

    def BFS(self,s):
        Q = Queue()
        Q.push(s)
        self.parent[s] = None
        self.visited[s-1] = True

        while not Q.isEmpty():
            #print "the present queue is "
            #Q.printq()
            #print "now distance from source node is"
            #print self.dist[1:12]
            u = Q.pop()
            print "(%r -> %r)" %(self.parent[u],u)
            for v in self.graph[u]:
                if self.visited[v-1] == False:
                    self.visited[v-1] = True
                    Q.push(v)
                    self.parent[v] = u

a = Solution(graph6)
a.BFS(8)

