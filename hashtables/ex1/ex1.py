#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for weight, index in enumerate(weights):
        hash_table_insert(ht, index, weight)

    if len(weights) < 2:
        return None
    elif len(weights) == 2 and weights[0] == weights[1]:
        return (1, 0)
    else:
        weights_list = []
        for weight in weights:
            print("retrieve: ", hash_table_retrieve(ht, limit - weight))
            print("limit minus weight: ", limit-weight)
            if hash_table_retrieve(ht, limit - weight) is not None:
                weights_list.append(hash_table_retrieve(ht, limit - weight))

        weights_list.sort(reverse=True)
        weights_tuple = tuple(weights_list)
        print("weights tuple at 0: ", weights_tuple[0])
        print("weights tuple at 1: ", weights_tuple[1])
        print("weights tuple: ", weights_tuple)
        ht.print()
        return weights_tuple


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
