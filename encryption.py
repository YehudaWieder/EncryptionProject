from math import ceil

def transposition(message, key):
    print(len(message))

    encryption_message =  ""
    for i in range(ceil(len(message) // key) + 1):
        for j in range(i, len(message), ceil(len(message) // key) + 1):
            encryption_message += message[j]

    print(encryption_message)
    print(len(encryption_message))
    return encryption_message

transposition("WE ARE DISCOVERED FLEE AT ONCE", 6)

# def encryption(inputs):
#     method = inputs[0]
#     if method == "Transposition":
#        return transposition(inputs[1], inputs[2])