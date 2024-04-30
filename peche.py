from random import randint, seed

def record_shuffle(l):
    swaps = []
    for i in range(len(l)):
        j = randint(0, len(l) - 1)
        swaps.append((i, j))
        l[i], l[j] = l[j], l[i]
    return swaps

def unshuffle(l, swaps):
    for i, j in reversed(swaps):
        l[i], l[j] = l[j], l[i]
    return l

shuffled_flag = list('dFREEA5NImEg8xuZs9lFJSIDkPy2ojv}{u4gGc')
seed(42)
swaps = record_shuffle(list('JFFI{%s}' % ''.join(['a' for _ in range(32)])))  # We only care about the swaps, not the values
unshuffled_flag = unshuffle(shuffled_flag, swaps)

print(''.join(unshuffled_flag))