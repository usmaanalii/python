# Calculating AT content
dna_seq = "ACTGATCGATTACGTATAGTATTTGAATTCATCATACATACATACATATATCGTCGCGTTCAT"

A_count = dna_seq.count("A")
T_count = dna_seq.count("T")
AT_count = A_count + T_count

print("A count: " + str(A_count))
print("T count: " + str(T_count))
print("AT count: " + str(AT_count))

# Complementing DNA
replacement1 = dna_seq.replace('A', 't')
replacement2 = replacement1.replace('T', 'a')
replacement3 = replacement2.replace('C', 'g')
replacement4 = replacement3.replace('G', 'c')

print('The complementary DNA is ' + replacement4.upper() + '\n')


# Restriction fragment lengths
def restriction(sequence, cut):
    cut_off = sequence.find(cut)  # 24
    pre = sequence[0:cut_off]
    post = sequence[cut_off + 1:len(sequence)]

    print('The length of the first fragment is ' + str(len(pre)))
    print('The length of the second fragment is ' + str(len(post)))

restriction(dna_seq, 'GAAT')

# splicing out introns, part one
genomic_dna = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'

exon_1 = genomic_dna[0:62]
exon_2 = genomic_dna[90:10000]
coding_percentage = round((((len(exon_1) + len(exon_2)) / len(genomic_dna)) * 100), 2)

print('The coding DNA is ' + exon_1 + exon_2)
print('The percentage of coding DNA is ' + str(coding_percentage) + '%\n')

print('Coding bases in uppercase:\n' + exon_1.lower() + genomic_dna[63:91] + exon_2.lower())
