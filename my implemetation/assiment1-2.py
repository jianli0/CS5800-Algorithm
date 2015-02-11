import math
def function(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    else:
        return ( math.ceil(math.sqrt(n)) + 5 * function(math.floor(4.0/7*n))
                + 10 * function(math.floor(1.0/5*n)))


for i in range(1,11):
    print  str(int(function(i)))+",",
