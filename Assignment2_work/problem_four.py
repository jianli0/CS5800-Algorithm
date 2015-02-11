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

graph4= {1:[2,4],
        2:[7,8],
        3:[8],
        4:[7],
        5:[9,10],
        6:[2,8],
        7:[3,10],
        8:[7],
        9:[1],
        10:[3,6]
        }

def findCycle(graph,node):
    frontier = Stack()

    explored = []

    while True:
        if frontier.isEmpty():
            return False
        item = frontier.pop()
        frontier.

