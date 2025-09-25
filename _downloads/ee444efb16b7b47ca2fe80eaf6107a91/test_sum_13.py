"""

Test driven development:

Example from Coding Bat: List-2 > sum13

https://codingbat.com/prob/p167025

Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


The tests that are used on codingbat:

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
sum13([1, 2, 13, 2, 1, 13]) → 4
sum13([13, 1, 2, 13, 2, 1, 13]) → 3
sum13([]) → 0
sum13([13]) → 0
sum13([13, 13]) → 0
sum13([13, 0, 13]) → 0
sum13([13, 1, 13]) → 0
sum13([5, 7, 2]) → 14
sum13([5, 13, 2]) → 5
sum13([0]) → 0
sum13([13, 0]) → 0 
"""

import pytest

from sum_13 import sum13


# Using the nifty pytest.parametrize, so we only have to write one test

test_data = [
    ([1, 2, 2, 1], 6),
    ([1, 1], 2),
    ([1, 2, 2, 1, 13], 6),
    ([1, 2, 2, 1], 6),
    ([1, 1], 2),
    ([1, 2, 2, 1, 13], 6),
    ([1, 2, 13, 2, 1, 13], 4),
    ([13, 1, 2, 13, 2, 1, 13], 3),
    ([], 0),
    ([13], 0),
    ([13, 13], 0),
    ([13, 0, 13], 0),
    ([13, 1, 13], 0),
    ([5, 7, 2], 14),
    ([5, 13, 2], 5),
    ([0], 0),
    ([13, 0], 0),
    # These are not part of original test suite
    #   uncomment them, and see if your solution still passes.
    # ([3, 13, 13, 2, 5], 8),
    # (iter([13, 1, 2, 13, 2, 1, 13]), 3), #  Does it work with an iterable?
    ]

@pytest.mark.parametrize('nums, result', test_data)
def test_sum13(nums, result):
    assert sum13(nums) == result



                              
