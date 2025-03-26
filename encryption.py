from math import ceil

def transposition(path, key):
    print(len(path))

    encryption_message =  ""
    for i in range(ceil(len(path) // key) + 1):
        for j in range(i, len(path), ceil(len(path) // key) + 1):
            encryption_message += path[j]

    print(encryption_message)
    print(len(encryption_message))
    return encryption_message

transposition("WE ARE DISCOVERED FLEE AT ONCE", 6)

