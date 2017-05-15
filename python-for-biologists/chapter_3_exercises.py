# splitting genomic dna
import os
os.chdir('')  # input working directory where the files are located

dna_file = open('genomic_dna.txt')
contents = dna_file.read()

print(contents)

coding_file = open('coding_file.txt', 'w')
coding_file.write(contents[0:62] + contents[90:10000])

non_coding_file = open('non_coding_file.txt', 'w')
non_coding_file.write(contents[63:90])

# writing a FASTA file
FASTA_file = open('FASTA_file.txt', 'w')

headers = ['ABC123', 'DEF456', 'HIJ789']
sequences = ['ATCGTACGATCGATCGATCGCTAGACGTATCG',
             'actgatcgacgatcgatcgatcacgact', 'ACTGAC-ACTGT--ACTGTA----CATGTG']

FASTA_file.write(('>' + headers[0] + '\n' + sequences[0]) + '\n')
FASTA_file.write(('>' + headers[1] + '\n' + sequences[1].upper()) + '\n')
FASTA_file.write(('>' + headers[2] + '\n' +
                 sequences[2].replace('-', '')) + '\n')
