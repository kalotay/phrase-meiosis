#hamming distance implementation

def hamming_distance(string1, string2):
    #check the strings have the same length
    assert len(string1) == len(string2)
    return sum(1 for x, y in zip(string1, string2) if x != y)
