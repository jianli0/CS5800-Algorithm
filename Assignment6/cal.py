seq1 = ['U', 'A', 'A', ' ', ' ', 'G', ' ', 'G', 'U', 'G', 'C', 'A', 'U', 'C', 'U', 'A', 'G', 'U', 'G', 'C', 'U', 'G', 'U', 'U', 'A', 'G']
seq2 = ['U', 'A', 'A', 'G', 'U', 'G', 'C', 'G', 'U', 'G', 'C', 'A', 'U', 'G', 'U', 'A', ' ', 'U', ' ', 'A', 'U', 'G', ' ', 'U', ' ', 'G']
def cal(seq1,seq2):
    sum_ = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            sum_ += 2
        elif seq1[i] == " " or seq2[i] == " ":
            sum_ += -2
        else:
            sum_ += -3
    print sum_

cal(seq1,seq2)


