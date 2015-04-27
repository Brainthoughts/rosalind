__author__ = 'hannes'


"""
Given: Six positive integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
"""


input = '19253 17232 17090 18999 18873 17565'

nr_of_offspring = 2
data = input.split(' ')

gtypes = ['AA-AA', 'AA-Aa', 'AA-aa', 'Aa-Aa', 'Aa-aa', 'aa-aa']
probabilities = {'AA-AA':1, 'AA-Aa':1, 'AA-aa':1, 'Aa-Aa':0.75, 'Aa-aa':0.5, 'aa-aa':0}

expected_offspring = 0.0
for index, count in enumerate(data):
    expected_offspring += nr_of_offspring * float(count) * probabilities[gtypes[index]]

print(expected_offspring)

