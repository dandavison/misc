import math


def carrier_freq_from_prev(prev):
    mutant_allele_freq = math.sqrt(prev)
    wildtype_allele_freq = 1 - mutant_allele_freq
    return 1 - (wildtype_allele_freq ** 2)
