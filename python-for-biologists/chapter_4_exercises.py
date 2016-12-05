# processing DNA in a file
import os
os.chdir('') # input directory where the files are located

dna_file = open('input.txt')

new_dna_file = open('cleaned_dna.txt', 'w')

for sequence in dna_file:
    cleaned_dna = sequence[15:len(sequence)]
    new_dna_file.write(cleaned_dna)
    print('processed sequence with new length ' + str(len((cleaned_dna))))

print('\n')

# multiple exons from genomic DNA
genomic_dna_file = open('genomic_dna.txt')
positions_file = open('exons.txt')

genomic_dna = genomic_dna_file.read()

coding_sequence = ''

i = 0

for line in positions_file:
    cleaned = line.split(',')
    i = i + 1
    # Start and stop are initially strings extracted from the txt file
    start = int(cleaned[0])
    stop = int(cleaned[1])

    exon = genomic_dna[start:stop]
    coding_sequence = coding_sequence + exon

    print('The coding sequence after slice ' + str(i) + ' is: ' + coding_sequence)


coding_sequence_file = open('coding_sequences.txt', 'w')
coding_sequence_file.write(coding_sequence)
coding_sequence_file.close()
