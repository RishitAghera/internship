from itertools import chain, combinations

def powerset(items):
    return chain.from_iterable(combinations(items, r) for r in range(len(items)+1))

def maximum_value(maximum_weight, items):
    result = 0
    for choice in powerset(items):
        weight = sum(map(lambda x: x['weight'], choice))
        if weight > maximum_weight:
            continue
        value = sum(map(lambda x: x['value'], choice))
        if value > result:
            result = value
    return result