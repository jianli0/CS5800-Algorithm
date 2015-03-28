seq1 = ['U', 'A', 'A', 'G', 'G', 'U', 'G', 'C', 'A', 'U', 'C', 'U', 'A', 'G', 'U', 'G', 'C', 'U', 'G', 'U', 'U', 'A', 'G']
seq2 = ['U', 'A', 'A', 'G', 'U', 'G', 'C', 'G', 'U', 'G', 'C', 'A', 'U', 'G', 'U', 'A', 'U', 'A', 'U', 'G', 'U', 'G']
operation = ['d', 'u', 'd', 'u', 'd', 'd', 'd', 'u', 'd', 'u', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'l', 'd', 'l', 'l', 'd', 'd', 'd']

def match(seq1,seq2,operation):
    pointer1 = len(seq1) -1
    pointer2 = len(seq2) -1
    for i in operation:
        if i == "d":
            pointer1 -= 1
            pointer2 -= 1
            print "(p1-%d,p2-%d)"%(pointer1,pointer2)
        if i == "u":
            pointer1 -= 1
            seq2.insert(pointer2+1," ")
        if i == "l":
            pointer2 -= 1
            seq1.insert(pointer1+1," ")
    print_seq(seq1)
    print_seq(seq2)

def print_seq(seq):
    for i in seq:
        print i,
    print

match(seq1,seq2,operation)







