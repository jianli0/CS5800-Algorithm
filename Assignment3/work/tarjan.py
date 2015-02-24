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

    def printStack(self):
        print "   stack is %r"%(self.list)

class Solution:
    def __init__(self):
        self.visited = []
        self.pre = []
        self.post = []
        self.clock = 1
        self.treeedges = []
        self.LOW = []
        self.isRemoved = []
        self.mystack = Stack()

        for i in range(11):
            self.visited.append(False)
            self.pre.append(None)
            self.post.append(None)
            self.LOW.append(None)
            self.isRemoved.append(None)

    def dfs(self,graph,depth):
        for u in graph.keys():
            if not self.visited[u]:
                self.explore(graph,u,depth)

    def explore(self,graph,v,depth):
        self.visited[v] = True
        print "%d  visited[%d] sets True" %(depth,v)
        self.previsit(v)
        for u in graph[v]:
            if not self.visited[u]:
                self.treeedges.append((v,u))
                self.explore(graph,u,depth + 1)
            self.traverse(v,u)
        self.postvisit(v)

    def previsit(self,v):
        self.pre[v] = self.clock
        self.LOW[v] = self.pre[v]
        self.clock += 1
        self.mystack.push(v)
        self.isRemoved[v] = False
        print "   pre[%d] sets to %d"%(v,self.pre[v])
        print "   LOW[%d] sets to %d"%(v,self.LOW[v])
        print "   push %d to stack"%(v)
        self.mystack.printStack()
        print "   isRemoved[%d] sets to False"%(v)


    def traverse(self,v,u):
        print "   now traversing edge(%d,%d)"%(v,u)
        print "   treeedges are now %r"%(self.treeedges)
        if (v,u) in self.treeedges :
            self.LOW[v] = min(self.LOW[v],self.LOW[u])
            print "   %d LOW now is %d"%(v,self.LOW[v])
        elif self.isRemoved[u] == False:
            self.LOW[v] = min(self.LOW[v], self.pre[u])
            print "   isReomved[%d] is False, in stack"%(u)
            print "   %d LOW now is %d"%(v,self.LOW[v])

    def postvisit(self,v):
        if self.LOW[v] == self.pre[v]:
            print "   self.LOW[%d] == self.pre[%d]"%(v,v)
            C = []
            while True:
                w = self.mystack.pop()
                print "   stack pop"
                self.mystack.printStack()
                C.append(w)
                self.isRemoved[w] = True
                print "   isRemoved[%d] sets true"%(w)
                if w == v:
                    break
            print "---a new SCC is %r---"%(C)

a = Solution()
a.dfs(graph_plus,1)
'''

b = Solution()
b.dfs(graph5, 1)
'''




