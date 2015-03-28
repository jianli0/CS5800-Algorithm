graph = {1:{1:0,2:float("inf"),3:float("inf"),4:-1,5:-2},
         2:{1:float("inf"),2:0,3:float("inf"),4:3,5:5},
         3:{1:float("inf"),2:4,3:0,4:float("inf"),5:5},
         4:{1:float("inf"),2:3,3:4,4:0,5:float("inf")},
         5:{1:float("inf"),2:4,3:4,4:float("inf"),5:0}
        }

graph_test = {1:{1:0,2:-3,3:-2,4:2},
              2:{1:float("inf"),2:0,3:4,4:2},
              3:{1:float("inf"),2:-2,3:0,4:5},
              4:{1:float("inf"),2:float("inf"),3:5,4:0},
            }

class Solution:
    def __init__(self,graph):
        self.graph = graph
        self.table_num = 0

    def aps(self):
        print "---Table %d---"%(self.table_num)
        self.printgraph()

        nodes = self.graph.keys()
        for k in nodes:
            self.table_num += 1
            for i in nodes:
                for j in nodes:
                    if self.graph[i][k] + self.graph[k][j] < self.graph[i][j]:
                        self.graph[i][j] = self.graph[i][k] + self.graph[k][j]
            print "---Table %d---"%(self.table_num)
            self.printgraph()

    def printgraph(self):
        for i in self.graph.keys():
            for j in self.graph[i].keys():
                print "%3r"%(self.graph[i][j]),
            print


# a = Solution(graph_test)
# a.aps()

b = Solution(graph)
b.aps()
