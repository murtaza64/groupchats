from itertools import combinations
from random import choice, shuffle
names = ['Amrita', 'Arnav L', 'Arnav M', 'Chloe', 'Craig', 'Ellen', 'Georgina', 'Hriday', 'Humza', 'Kabir', 'Murtaza', 'Oh Jun', 'Ramzi', 'Sadhana', 'Satadru', 'Seungho', 'Sophie', 'Tara', 'Will']
k = 0
nouns = [word.strip() for word in open('nouns.txt')]
adjectives = [word.strip() for word in open('adjectives.txt')]
groupgen = (sorted(group) for i in range(2, len(names) - 1) for group in combinations(names, i))
groups = []

for group in groupgen:
    noun = choice(nouns)
    if noun[-1] in 'iy':
        noun = noun[:-1] + 'ies'
    elif noun[-1] in 'szx':
        noun += 'es'
    else:
        noun += 's'
    groups.append((choice(adjectives).upper() + ' ' + noun.upper(), group))

shuffle(groups)
groups.insert(0, ('JUSTICE LEAGUE', names))
for group in groups:
    print(group[0])
    for name in group[1]:
        print(' ' + name)
    print()
