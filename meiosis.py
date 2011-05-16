import random as rn
import string
import hammingdist as hd

#all possible characters
ALPHABET = ' '.join([string.lowercase, string.punctuation])

class EvolvingPhrase:
    def _init_(self, phrase, cell_death_age):
        assert cell_death_age > 0
        self._phrase_ = phrase
        self._cell_death_age_ = int(cell_death_age)
        self._age_ = 0

    def update_fitness(self, target):
        if self._age_ < self._cell_death_age_:
            self._fitness_ = fitness(self._phrase_, target)
        else:
            self._fitness_ = 0

    def get_suitability(self, partner, target):
        return (fitness(partner._phrase_, target) +
            hd.hammingdist(self._phrase_, partner._phrase_))

    def take_step(self):
        self._age_ += 1

def fitness(phrase, target):
#fitness of a phrase
#defined as the phrase length minus the Hamming distance to target
    assert len(phrase) == len(target)
    return len(phrase) - hd.hamming_distance(phrase, target)

def mutate(phrase, rate):
#mutates a phrase
#each character has a probability 'rate' of mutation to any random character
    assert 0.0 <= rate <= 1.0
    for c in phrase:
        if rn.random() > rate:
            yield c
        else:
            yield rn.choice(ALPHABET)

def cross_breed(phrase1, phrase2, rate):
#cross between two phrases
#similar to meiosis
#produces two offsprings
    assert len(phrase1) == len(phrase2)
    assert 0.0 <= rate <= 1.0
    crosses = [rn.random() < rate for i in phrase1]
    n_crosses = 0
    for x, y, cross in zip(phrase1, phrase2, crosses):
        n_crosses += cross
        if n_crosses % 2:
            yield x, y
        else:
            yield y, x
