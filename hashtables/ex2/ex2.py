#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # loop over array, add tickets to hash table
    # add first flight to trip
    # loop over tickets to find each destination after

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    source_flight = hash_table_retrieve(hashtable, "NONE")
    route[0] = source_flight

    for i in (num + 1 for num in range(len(route)-1)):
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route
