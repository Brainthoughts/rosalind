__author__ = 'hannes'

# Given:
k = 21  # individuals are homozygous dominant for a factor,
m = 24  # heterozygous, and
n = 26  # homozygous recessive.


# Return P(F,F) + P(F,f)
# The probability that two randomly selected mating organisms
# will produce an individual possessing a dominant allele
# (and thus displaying the dominant phenotype).
# Assume that any two organisms can mate.

# K dominant homozygous (F,F)
# M dominant heterozygous (F,f)
# N recessive homozygous (f,f)

"""
There are t individuals in the population.

The probability of 2 dominant homozygous individuals mate P(K/K) = k/t * (k-1/t-1)
In P(K/K) 100% of the offspring will be F/F -> P(FF/(K/K)) = 1
        P(F*/(K/K)) = 1

The probability of 1 dominant homozygous and 1 recessive homozygous individual mate P(K/N) = k/t * (n/t-1)
In P(K/N) 100% of the offspring will be F/f -> P(Ff/(K/N)) = 1
        P(F*/(K/N)) = 1

The probability of 1 dominant homozygous and 1 heterozygous individual mate P(K/M) = k/t * (m/t-1)
In P(K/M)  50% of the offspring will be F/f -> P(Ff/(K/M)) = 0.50
       and 50% of the offspring will be F/F -> P(FF/(K/M)) = 0.50
       P(F*/(K/M)) = 1

The probability of 2 heterozygous individuals mate P(M/N) = m/t * (m-1/t-1)
In P(M/M)  50% of the offspring will be F/f -> P(Ff/(M/M)) = 0.5
       and 25% of the offspring will be F/F -> P(FF/(M/M)) = 0.25
       P(F*/(M/M)) = 0.75

The probability of 1 recessive homozygous and 1 heterozygous individual mate P(M/N) = n/t * (m/t-1)
In P(N/M)  50% of the offspring will be F/f -> P(Ff/(N/M)) = 0.50
       and 50% of the offspring will be f/f -> P(ff/(N/M)) = 0.50
       P(F*/(N/M)) = 0.5

The probability of 2 recessive homozygous individuals mate P(N/N) = n/t * (n-1/t-1)
In P(N/N) 0% of the offspring will be F/F -> P(ff/(N/N)) = 1 -> P(FF/((N/N)) = 0
        P(F*/(N/N)) = 0
"""



t = sum([k, m, n])
pk = k / t
pm = m / t
pn = n / t


# Total probability
prob = 1
# Minus the probability of both parents being homozygous recessive
prob -= pn * ((n - 1) / (t - 1))
# Minus twice the probability of one being homozygous recessive and the other
# one heterozygous with the recessive allele (this is the 0.5)
prob -= 2 * pn * (m / (t - 1)) * 0.5
# Minus the probability of both being heterozygous with the recessive allele (this is the 0.25)
prob -= pm * ((m - 1) / (t - 1)) * 0.25
print(prob)