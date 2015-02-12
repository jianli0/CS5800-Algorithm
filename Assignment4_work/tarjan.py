graph5 = {1:[5,6],
        2:[],
        3:[4,7,10],
        4:[2],
        5:[4,7,8,10],
        6:[8],
        7:[5],
        8:[2,7,10],
        9:[1,3,4,8,10],
        10:[2,5]
        }
graph_plus = {1:[2,3],
        2:[4],
        3:[4,5],
        4:[1,6],
        5:[6],
        6:[]}

class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0

    def isIn(self,element):
        "Returns true if element is in stack"
        return (element in self.list)


class Tarjan:
    index = 0
    mystack = Stack()
    DFN = []
    LOW = []
    visited = []

    for i in range(11):
        DFN.append(None)
        LOW.append(None)
        visited.append(False)

    def tarjan(self,u,graph):
        self.index += 1
        self.DFN[u] = self.index
        self.LOW[u] = self.index
        self.mystack.push(u)

        for v in graph[u]:
            if not self.visited[v] :
                self.visited[v] = True
                self.tarjan(v,graph)
                self.LOW[u] = min(self.LOW[u],self.LOW[v])
            elif self.mystack.isIn(v):
                self.LOW[u] = min(self.LOW[u], self.DFN[v])

        if(self.DFN[u] == self.LOW[u]):
            print "a new SCC is "
            print "# for test : current u is %d"%(u)
            while True:
                v = self.mystack.pop()
                print v
                if u == v:
                    break

a = Tarjan()
a.tarjan(1,graph_plus)







