'''
Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger) string Genome if there is an interval of Genome of length L in which Pattern appears at least t times. For example, TGCATGCA forms a (25,3)-clump in the following Genome: gatcagcataagggtcccTGCAATGCATGACAAGCCTGCAgttgttttacgatcagcataagggtcccTGCAATGCATGACAAGCCTGCAgttgttttac.

Clump Finding Problem
Find patterns forming clumps in a string.

Given: A string Genome, and integers k, L, and t.

Return: All distinct k-mers forming (L, t)-clumps in Genome.

http://rosalind.info/problems/ba1e/
'''


import re
from collections import defaultdict

#s="CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"


# k = 5
# L = 75
# t = 4

data = list(open("/home/am/Downloads/rosalind_ba1e.txt",'r'))
s=data[0]
k,L,t =(int(x) for x in data[1].split())

print('k=',k,'L=',L,'t=',t,'\n')

str_cnt = defaultdict(int)

#print(len(s))

str_slice = [s[i:i+L] for i in range(0,len(s),L-k)]

# print(str_slice)
for i in(str_slice):
    #print(i)
    b = [i[j:j+k] for j in range(len(i)-(k-1))]
    #print(b)

    for kk in b:
        str_cnt[kk] +=1

#print(sorted(str_cnt.values()))
for key, val in str_cnt.items():
    if(val>=t):
        print(key)




