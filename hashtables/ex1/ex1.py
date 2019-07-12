#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


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
    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
