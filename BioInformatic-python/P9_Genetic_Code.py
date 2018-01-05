'''
Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string ss corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by ss.

http://rosalind.info/problems/prot/

'''


import RNA_codon_table

rnacode = RNA_codon_table.RNA_codon_table()

data = list(open("/home/am/Downloads/rosalind_prot.txt",'r'))
dna=data[0]




s="ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
xrna="MAMAPRTEINSTRING"

dna_t2u = dna.replace('T','U')
rna =[]
#print(ss)
for i in range(0,len(dna_t2u)-2,3):
    t=dna_t2u[i:i+3]
    #print(t)

    rna.append(rnacode.rna(dna_t2u[i:i+3]))

#print(len(rna))
#print("".join(rna))
#print(rna)

rna_arr = []
temp = []

for i in rna:
    if i !='Stop':
        temp.append(i)
    else:
        rna_arr.append("".join(temp))
        temp= []


rna_arr = list(filter(("").__ne__, rna_arr))

print("".join(rna_arr))
