'''
Problem
For positive integers aa and nn, aa modulo nn (written amodnamodn in shorthand) is the remainder when aa is divided by nn. For example, 29mod11=729mod11=7 because 29=11×2+729=11×2+7.

Modular arithmetic is the study of addition, subtraction, multiplication, and division with respect to the modulo operation. We say that aa and bb are congruent modulo nn if amodn=bmodnamodn=bmodn; in this case, we use the notation a≡bmodna≡bmodn.

Two useful facts in modular arithmetic are that if a≡bmodna≡bmodn and c≡dmodnc≡dmodn, then a+c≡b+dmodna+c≡b+dmodn and a×c≡b×dmodna×c≡b×dmodn. To check your understanding of these rules, you may wish to verify these relationships for a=29a=29, b=73b=73, c=10c=10, d=32d=32, and n=11n=11.

As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)


http://rosalind.info/problems/mrna/

'''


import RNA_codon_table
from collections import defaultdict
import collections

# rnaCodon_sorted:
# Position : ran, aa
# 1: ('A', ['GCA', 'GCC', 'GCG', 'GCU']),
# 2: ('C', ['UGU', 'UGC']),
# 3: ('D', ['GAU', 'GAC']),
# 4; ('E', ['GAG', 'GAA']),
# 5: ('F', ['UUU', 'UUC']),
# 6: ('G', ['GGG', 'GGA', 'GGU', 'GGC']),
# 7: ('H', ['CAU', 'CAC']),
# 8: ('I', ['AUC', 'AUA', 'AUU']),
# 9: ('K', ['AAA', 'AAG']),
# 10: ('L', ['CUU', 'CUC', 'CUG', 'CUA', 'UUG', 'UUA']),
# 11: ('M', ['AUG']),
# 12: ('N', ['AAU', 'AAC']),
# 13: ('P', ['CCU', 'CCG', 'CCA', 'CCC']),
# 14: ('Q', ['CAA', 'CAG']),
# 15: ('R', ['CGA', 'CGG', 'AGA', 'AGG', 'CGC', 'CGU']),
# 16: ('S', ['UCC', 'UCU', 'UCA', 'UCG', 'AGC', 'AGU']),
# 17: ('Stop', ['UGA', 'UAA', 'UAG']),
# 18: ('T', ['ACC', 'ACA', 'ACG', 'ACU']),
# 19: ('V', ['GUG', 'GUA', 'GUC', 'GUU']),
# 20: ('W', ['UGG']),
# 21: ('Y', ['UAC', 'UAU'])]


rnacode = RNA_codon_table.RNA_codon_table()

data = list(open("/home/am/Downloads/rosalind_mrna.txt",'r'))
rna=data[0].replace("\n", "")
#rna = 'MA'
# print(rnacode.rna("AUG"))

rnaCodon = defaultdict(list)

for k,v in rnacode.rnacode.items():
    rnaCodon[v].append(k)

rnaCodon_sorted = collections.OrderedDict(sorted(rnaCodon.items()))
rnaCodon_sorted = list(rnaCodon_sorted.items())

rnaPosition = {}
rnaCombo = {}

for i in range(0,len(rnaCodon_sorted)):
    rnaPosition[rnaCodon_sorted[i][0]] = i+1
    rnaCombo[rnaCodon_sorted[i][0]] = len(rnaCodon_sorted[i][1])

#print(rnaPosition)
#print(rnaCombo)

tpos = 0
tcombo = 1
tt = 0

for i in rna:
    #print(i, " --> ",rnaPosition[i])
    tpos += rnaPosition[i]
    tcombo *= rnaCombo[i]
    tt += rnaPosition[i] * rnaCombo[i]

tpos= tpos + rnaPosition['Stop']

tpos = tpos%1000000
print("tpos = ",tpos)

tcombo= tcombo * rnaCombo['Stop']

tcombo = tcombo%1000000
print("tcombo = ",tcombo)

tt= tt + rnaCombo['Stop']*rnaPosition['Stop']
print("tt = ",tt%1000000)


