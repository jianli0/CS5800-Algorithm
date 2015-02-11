def Fibonacci(n,depth):
    depth = depth + 1
    if n == 0:
        print "current depth is:%d"%(depth)
        return 0
    if n == 1:
        print "current depth is:%d"%(depth)
        return 1
    if n > 1:
        return Fibonacci(n - 1,depth) + Fibonacci(n - 2,depth)
    else:
        return False

#print Fibonacci(5,-1)

print Fibonacci(10,-1)


