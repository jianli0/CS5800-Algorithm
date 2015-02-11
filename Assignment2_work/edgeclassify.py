graph1 = {1 : [4,5,6],
        2 : [3,4,7,9],
        3 : [2,10],
        4 : [1,2,6],
        5 : [1,7,9],
        6 : [1,4,8,9,10],
        7 : [2,5,8],
        8 : [6,7,9,10],
        9 : [2,5,6,8],
        10 : [3,6,8]}
pre1 = [0, 1, 3, 4, 2, 9, 6, 8, 7, 10, 5]
post1 = [0, 20, 18, 17, 19, 12, 15, 13, 14, 11, 16]

graph2 = {1 : [3,4,10],
        2 : [8],
        3 : [4],
        4 : [],
        5 : [2,10],
        6 : [10],
        7 : [3,4,10],
        8 : [3],
        9 : [2,3,4,5,8],
        10 : [3,4,8]}

pre2 = [0, 1, 11, 2, 3, 13, 15, 17, 7, 19, 6]
post2 = [0, 10, 12, 5, 4, 14, 16, 18, 8, 20, 9]

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

pre4 = [0, 1, 2, 4, 14, 17, 9, 3, 5, 18, 8]
post4 = [0, 16, 13, 7, 15, 20, 10, 12, 6, 19, 11]
def edgeclassify(graph,pre,post):
    forward = []
    back = []
    cross = []
    for u in graph.keys():
        for v in graph[u]:
            if pre[u] < pre[v] < post[v] < post[u]:
                forward.append((u,v))
            elif pre[v] < pre[u] < post[u] < post[v]:
                back.append((u,v))
            elif pre[v] < post[v] < pre[u] < post[u]:
                cross.append((u,v))
    print "forward is :"
    print forward
    print "back is :"
    print back
    print "cross is "
    print cross


#edgeclassify(graph1,pre1,post1)
#
#edgeclassify(graph2,pre2,post2)
edgeclassify(graph4,pre4,post4)
