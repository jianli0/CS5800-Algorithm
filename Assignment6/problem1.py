seq1 = "UAAGGUGCAUCUAGUGCUGUUAG"
seq2 = "UAAGUGCGUGCAUGUAUAUGUG"

class Solution:
    def __init__(self,seq1,seq2):
        self.seq1 = seq1
        self.seq2 = seq2
        self.table = []
        self.direction = []

        for i in range(len(self.seq1)+1):
            self.table.append([])
            self.direction.append([])
            for j in range(len(self.seq2)+1):
                self.table[i].append(-float("inf"))
                self.direction[i].append("")

        for j in range(len(self.seq2)+1):
            self.table[0][j] = -2*j
            self.direction[0][j] = "<"

        for i in range(len(self.seq1)+1):
            self.table[i][0] = -2*i
            self.direction[i][0] = "^"

        self.direction[0][0] = 0

    def max_score(self):
        for i in range(1,len(self.seq1)+1):
            for j in range(1,len(self.seq2)+1):
                #print "i:%d j:%d"%(i,j)
                self.table[i][j] = max(self.table[i-1][j]-2,\
                        self.table[i][j-1]-2,\
                        self.table[i-1][j-1] + self.cal_score(i,j))
                if self.table[i][j] == self.table[i-1][j]-2:
                    self.direction[i][j] += "^"
                if self.table[i][j] == self.table[i][j-1]-2:
                    self.direction[i][j] += "<"
                if self.table[i][j] == (self.table[i-1][j-1] + self.cal_score(i,j)):
                    self.direction[i][j] += "d"

    def cal_score(self,i,j):
        '''for sequence index starts from 0'''
        if self.seq1[i-1] == self.seq2[j-1]:
            return 2
        else:
            return -3

    def get_table(self):
        for i in range(len(self.seq1)+1):
            for j in range(len(self.seq2)+1):
                print "%3d"%self.table[i][j],
            print

    def get_dir_table(self):
        for i in range(len(self.seq1)+1):
            for j in range(len(self.seq2)+1):
                print "%3s"%self.direction[i][j],
            print

    def get_max_score(self):
        max_scores = []
        for i in range(len(self.seq1)+1):
            max_scores.append(max(self.table[i]))
        return max(max_scores)



a = Solution(seq1,seq2)
a.max_score()
a.get_table()
a.get_dir_table()

