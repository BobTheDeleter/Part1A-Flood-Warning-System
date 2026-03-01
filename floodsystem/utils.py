# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""


def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple::

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple::

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)

#deals with ones with equal values
import heapq
def get_n_largest(N, things_numbers):
   sorted_things_numbers = heapq.nlargest(N, things_numbers, key=lambda x: x[1])
   numbers_list = [thing_number[1] for thing_number in things_numbers]
   things_list = [thing_number[0] for thing_number in things_numbers]
   for i in range(numbers_list):
      number = numbers_list[i]
      thing = things_list[i]
      if number == sorted_things_numbers[-1][1]:
        if (thing, number) not in sorted_things_numbers:
            sorted_things_numbers.append((thing, number))