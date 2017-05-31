def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count_n = 0

    for i in dna:
        if nucleotide == i:
            count_n += 1

    return count_n
        


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1


def is_valid_sequence(dna):
    """(str)->bool

    Return True if DNA sequence has only valid ATCG letters.

    >>> is_valid_sequence('ATCGGC')
    Trune
    >>> is_valid_sequence('AHTC')
    False
    """
    valid = True
    
    for i in dna:
        if i not in 'ATCG':
            valid = False

    return valid


def insert_sequence(dna1, dna2, pos):
    """(srt,str,int) -> str

    Return string of dna1 inserted in dna1 at specified position.

    >>> insert_sequence('CCGG','AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG','AT',0)
    'ATCCGG'
    >>> insert_sequence('CATGG','CCA', 5)
    'CATGGCCA
    """

    new_dna = dna1[:pos] + dna2 + dna1[pos:] 

    return new_dna
    
def get_complement(dna):
    """(str)->str

    Return the DNA complement for each DNA in given string.

    >>>get_complement('A')
    'T'
    >>>get_coplement('T')
    'A'
    >>>get_coplement('G')
    'C'
    """
    
    if dna == 'A':
        return 'T'
    elif dna == 'T':
        return 'A'
    elif dna == 'C':
        return 'G'
    elif dna == 'G':
        return 'C'
        
def get_complementary_sequence(dna):
    """(str)->str 
    
    Return the complement DNA sequence for the input.
    
    >>>get_complementary_sequence('AT')
    'TA'
    >>>get_complementary_sequence('GATTACT')
    'CTAATGA'
    """
    
    comp = ''
    
    for i in dna:
        comp = comp + get_complement(i)
        
    return comp
