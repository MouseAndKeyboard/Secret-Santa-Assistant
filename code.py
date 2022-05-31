from itertools import permutations
import math


def derangements(n):
    'All deranged permutations of the integers 0..n-1 inclusive'
    return (perm for perm in permutations(range(n))
             if all(indx != p for indx, p in enumerate(perm)))

def apply_permutation(permutation, items):
    'Applies a permultation to a list of items'
    output = [0]*len(items)
    for i, dst in enumerate(permutation):
        output[dst] = items[i]

    return output

def power_apply(permutation, items, times):
    result = items
    for _ in range(times):
        result = apply_permutation(permutation, result)
    return result

def power(permutation, times):
    return power_apply(permutation, range(0, len(permutation)), times)

def check_if_valid(permutation):
    result = power(permutation, 2)
    for i, dst in enumerate(result):
        if i == dst:
            return False

    return True

n = int(input("How many participants? "))
permutations = derangements(n)

names = ['']*n
for i in range(n):
    names[i] = input(f'Please give person {i} a name: ')

valid_permutations = list(filter(check_if_valid, permutations))

print('You will now enter any extra information you know')
adding_knowns = True
musthave_constraints = []

while(adding_knowns):
    yn = input('Do you want to add a known gifter? (y/n)')
    if yn == 'y':
        for i, name in enumerate(names):
            print(f'[{i}] {name}')
        gifter = int(input('Please enter the INDEX of the known gifter: '))
        receiver = int(input(f'Okay, who is {names[gifter]} gifting to (INDEX): '))
        musthave_constraints.append([gifter, receiver])
    else:
        adding_knowns= False

for constraint in musthave_constraints:
    valid_permutations = list(filter(lambda perm: perm[constraint[0]] == constraint[1], valid_permutations))

adding_restricted = True

mustnothave_constraints = []
while(adding_restricted):
    yn = input('Do you want to restrict a known gifter? (y/n)')
    if yn == 'y':
        for i, name in enumerate(names):
            print(f'[{i}] {name}')
        gifter = int(input('Please enter the INDEX of the restricted gifter: '))
        receiver = int(input(f'Okay, who cant {names[gifter]} gift to (INDEX): '))
        mustnothave_constraints.append([gifter, receiver])
    else:
        adding_restricted = False

for constraint in mustnothave_constraints:
    valid_permutations = list(filter(lambda perm: perm[constraint[0]] != constraint[1], valid_permutations))

fromto = [[0]*n for i in range(n)]

print(list(valid_permutations))
for permutation in valid_permutations:
    for i in range(n):
        print(f'{names[i]} -> {names[permutation[i]]}')
        fromto[i][permutation[i]] += 1
    print()

print(len(valid_permutations))
print()
for row in fromto:
    print(row)



