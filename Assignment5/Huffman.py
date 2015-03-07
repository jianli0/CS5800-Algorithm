mystring = 'HABBIEIHIHAAHAEBGCHBBHICDHGCHIHBBGBBBBGGIGACHABHACIBCBGIIBBAIBAIABBBAIGEBBCBCBCBDACBBBBFAAGAAAAAFAFF'

import mypriorityqueue
from collections import OrderedDict

class Solution:
    def __init__(self,mystring):
        self.mystring = mystring
        self.frequency = {}
        self.heap = mypriorityqueue.PriorityQueue()


    def huffman(self):
        for (letter,freq) in self.getfrequency():
            self.heap.push(letter,freq)
        for k in range(len(self.getfrequency())):
            self.heap.printHeap()
            [i_freq,i] = self.heap.allpop()
            #print "i:%r,i_freq:%r"%(i,i_freq)
            [j_freq,j] = self.heap.allpop()
            self.heap.push((i,j),i_freq + j_freq)

    def removeduplicate(self):
        return list(set(self.mystring))

    def getfrequency(self):
        removed = self.removeduplicate()
        for i in removed:
            self.frequency[i] = self.mystring.count(i)
        sort_freq = OrderedDict(sorted(self.frequency.items(), key = lambda x:x[1])).items()
        return sort_freq


a = Solution(mystring)
a.huffman()
