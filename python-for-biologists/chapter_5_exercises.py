# Percentage of amino acid residues, part one
def get_percent(seq, residue):

    seq_length = len(seq)
    residue_count = (seq.upper().count(residue.upper()))

    return round((residue_count / seq_length) * 100)


assert get_percent("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert get_percent("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert get_percent("MSRSLLLRFLLFLLLLPPLP", "L") == 50
assert get_percent("MSRSLLLRFLLFLLLLPPLP", "Y") == 0


# Percentage of amino acid residues, part two
def get_percent_2(seq, residue_list=["A", "I", "L", "M", "F", "W", "Y", "V"]):

    seq_length = len(seq)

    residue_count = 0
    for residue in residue_list:
        residue_count += (seq.upper().count(residue.upper()))

    return round((residue_count / seq_length) * 100)


assert get_percent_2("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert get_percent_2("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert get_percent_2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert get_percent_2("MSRSLLLRFLLFLLLLPPLP") == 65
