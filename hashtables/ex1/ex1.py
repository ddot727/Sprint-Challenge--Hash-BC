#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # need an index
    # loop through weights, see what meets limit
    # add new weight to hash table
    # find difference between limit and new weight
    # if it's in hash table, thats what we need (other weight)
    # if new weight and other weight are at (0, 1), make 1 go first
    # else order pair with the larger index first
    # increment the index
    # return None if can't find a pair
    index = 0

    while index < length:
        new_weight = weights[index]
        hash_table_insert(ht, new_weight, index)
        needed = limit - new_weight
        other_weight = hash_table_retrieve(ht, needed)

        if other_weight:
            if index == 1:
                return (index, 0)
            elif other_weight > index:
                return (other_weight, index)
            else:
                return (index, other_weight)
        index += 1

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
