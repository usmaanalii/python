import re


# Accesion names
gene_names = ['xkn59438', 'yhdck2', 'eihd39d9',
              'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

print('Contains 5:')
for gene in gene_names:
    if re.search(r'5', gene):
        print(gene)

print('\nContains d or e:')
for gene in gene_names:
    if re.search(r'(d|e)', gene):  # | represents 'or'
        print(gene)

print('\nContains d with an e anywhere after it:')
for gene in gene_names:
    # . represents 'any character', * represents '0 or more'
    if re.search(r'(d.*e)', gene):
        print(gene)

print('\nContains d and e seperated by a single letter:')
for gene in gene_names:
    if re.search(r'(d[a-z]{1}e)', gene):  # textbook answer: d.e
        print(gene)

print('\nContains d and e in any order:')
for gene in gene_names:
    if re.search(r"d.*e", gene) or re.search(r"e.*d", gene):
        print(gene)

print('\nStarts with x or y:')
for gene in gene_names:
    if re.search(r'^(x|y)', gene):  # ^ represents 'starts with'
        print(gene)

print('\nStarts with x or y and ends with e:')
for gene in gene_names:
    # textbook answer: ^(x|y).*e$
    if re.search(r'^(x|y)', gene) and re.search(r'e$', gene):
        print(gene)

print('\nContains three or more numbers in a row:')
for gene in gene_names:
    if re.search(r'[0-9]{3,100}', gene):  # no space in {3,100}
        print(gene)

print('\nEnds with d followed by a, r or p:')
for gene in gene_names:
    if re.search(r'd[a|r|p]$.*', gene):
        print(gene)

# Double digest
dna = open('dna.txt').read().rstrip('\n')

cuts = [0]

for match in re.finditer(r"A[ATGC]TAAT", dna):
    cuts.append(match.start() + 3)

for match in re.finditer(r"GC[AG][AT]TG", dna):
    cuts.append(match.start() + 4)

cuts.append(len(dna))
cuts.sort()

print('\nFragment lengths:\n')
for i in range(1, len(cuts)):
    print(cuts[i] - cuts[i - 1])
