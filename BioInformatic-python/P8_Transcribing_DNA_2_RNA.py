'''
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string tt corresponding to a coding strand, its transcribed RNA string uu is formed by replacing all occurrences of 'T' in tt with 'U' in uu.

Given: A DNA string tt having length at most 1000 nt.

Return: The transcribed RNA string of tt.

http://rosalind.info/problems/rna/

'''

data = list(open("/home/am/Downloads/rosalind_rna.txt",'r'))
str=data[0]

str_new=str.translate(str.maketrans('T','U'))

print(str_new)
