array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]

NUM_PRIME = [2, 3, 5, 7]

def get_num(idFilter):
    ret = []

    idLookup = None
    if type(idFilter) == list:
        idLookup = idFilter
        idFilter = None
    elif type(idFilter) == int:
        idLookup = [idFilter]
        idFilter = None
    else:
        print("Invalid id parameters")

    for k, v in enumerate(array):
        if v in idLookup:
            ret.append(v)
    
    return ret

primes = get_num(NUM_PRIME)
print(array)
print(primes)