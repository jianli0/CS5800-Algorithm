seq1= [8, 17, 9, 4, 14, 19, 8, 1, 15, 9, 17, 4, 4, 10, 5, 8, 14, 19, 12, 14]
seq_test = [2,4,3,2,8,6,0,3,4,7]

class Solution:
    def __init__(self,seq):
        self.seq = seq
        self.lis = []
        self.parent = []
        for i in range(len(self.seq)):
            self.parent.append(None)

        self.lis_seq = []
        self.lis_seq_pos = []


    def lsis(self):
        self.lis.append(1)
        print "Longest at position %d is of length %d"%(1,self.lis[0])
        print "There is no previous position"
        for j in range(1,len(self.seq)):
            self.lis.append(1)
            for i in range(0,j):
                if self.seq[i] < self.seq[j] and self.lis[j] < self.lis[i] + 1:
                    self.lis[j] = self.lis[i] + 1
                    self.parent[j] = i
            print "Longest at position %d is of length %d"%(j+1,self.lis[j])
            if self.parent[j] == None:
                print "There is no previous position"
            else:
                print "The previous position is %r"%(self.parent[j]+1)

        print "The longest increasing subsequence has length %d"%(max(self.lis))

    def getparent(self):
        print "the parent list is %r"%(self.parent)
    def getstart(self):
        return self.lis.index(max(self.lis))

    def backtrack(self,end):
        self.lis_seq.append(self.seq[end])
        self.lis_seq_pos.append(end+1)
        if not self.parent[end] == None:
            self.backtrack(self.parent[end])

    def getlis_seq(self):
        print "one of the subsequences with the longest length is %r"%(self.lis_seq[::-1])

    def getlis_seq_pos(self):
        print "The positions of the entries in this sequence are %r"%(self.lis_seq_pos[::-1])

# a = Solution(seq_test)
# a.lsis()
# # a.getparent()
# # print a.getstart()
# a.backtrack(a.getstart())
# a.getlis_seq()
# a.getlis_seq_pos()

b = Solution(seq1)
b.lsis()
b.backtrack(b.getstart())
b.getlis_seq()
b.getlis_seq_pos()






