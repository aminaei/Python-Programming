'''
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string ss is the string scsc formed by reversing the symbols of ss, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string ss of length at most 1000 bp.

Return: The reverse complement scsc of ss.

http://rosalind.info/problems/revc/
'''

import re

#str='AAAACCCGGT'

data = list(open("/home/am/Downloads/rosalind_revc.txt",'r'))
str=data[0]

str_new=str.translate(str.maketrans('ACGT','TGCA'))

print(str_new[::-1])

