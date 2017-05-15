import os
os.chdir('')  # input directory where files are located

data_file = open('data.csv')


# AT Content
def get_percent(seq, residue_list=["A", "I", "L", "M", "F", "W", "Y", "V"]):

    seq_length = len(seq)

    residue_count = 0
    for residue in residue_list:
        residue_count += (seq.upper().count(residue.upper()))

    return residue_count / seq_length


for line in data_file:
    columns = line.rstrip("\n").split(",")
    species = columns[0]
    sequence = columns[1]
    name = columns[2]
    expression = columns[3]

    if get_percent(sequence, ['A', 'T']) > 0.65:
        print('high content: ' + name)
    elif get_percent(sequence, ['A', 'T']) < 0.45:
        print('low content: ' + name)
    else:
        print('med content: ' + name)
