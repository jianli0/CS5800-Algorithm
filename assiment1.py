import math
def function(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    else:
        return (n*n + function(math.ceil(n * 3.0/7)))

for i in range(1,10):
    print function(i)
