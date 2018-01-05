'''
Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

http://rosalind.info/problems/gc/
'''

import re

def fastaReader(fname):
    seq={}
    id = ''
    bases = ''
    newList = []
    cnt = 0
    with open(fname,'r') as f:
        lines = f.read().splitlines()

        for line in lines:
            if(line.startswith('>')):
                if(cnt != 0):
                    newList.append(bases)

                newList.append(line[1:])

                cnt = 1
                bases = ''

            else:
                bases = bases + line

        newList.append(bases)

        #print(newList)
        for i in range(0,len(newList),2):
            seq[newList[i]] = newList[i+1]


        #print(seq)
    return seq





seq = fastaReader("/home/am/Downloads/rosalind_gc.txt")

#print(seq)

Ros_seq = {}

for key,val in seq.items():
    cg_count = ((val.count('G')+val.count('C'))/len(val))*100
    Ros_seq[key]=cg_count
    #print(key,'',val,'',cg_count)

maxkey=max(Ros_seq, key=Ros_seq.get)

print(maxkey)
print(Ros_seq[maxkey])


