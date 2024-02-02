#!/usr/bin/python3
"""Practicing binary search in python
Binary Search is a search algorithm used in a sorted array by repeatedly
    dividing the search interval by half.

Explanation:
    Compare the middle element of the search space with the key.
    If the key is found at middle element, the process is terminated.
    If the key is not found at middle element, choose which half will be used
        as the next search space.
        If the key is smaller than the middle element, then the left side is
                used for next search.
        If the key is larger than the middle element, then the right side is
                used for next search.
    This process is continued until the key is found or the total search space
        is exhausted.

Time complexity: 
        Best case: O(1)
        Average case: O(log N)
        Worst case: O(log N)
Space complexity:
        iterative: O(1)
        recursive: O(log N)
"""


def iterative_binary_search(array: list, target: int) -> int:
    """Uses a while loop"""
    l = 0
    r = len(array) - 1
    while l < r:
        # get middle index
        m = (l + r) // 1

        # if found
        if array[m] == target:
            return m

        # if middle element is greater than target. right takes middle - 1
        if array[m] > target:
            r = m - 1

        # left takes middle + 1
        else:
            l = m + 1
    # Not found
    return -1


def recursive_binary_search(arr: list, targ: int, l: int, r: int) -> int:
    m = (l + r) // 2
    print(l, r, m, arr[m])
    if arr[m] == targ:
        return m
    elif arr[m] < targ:
        l = m + 1
        return recursive_binary_search(arr, targ, l, r)
    elif arr[m] > targ:
        r = m - 1
        return recursive_binary_search(arr, targ, l, r)
    else:
        return -1


if __name__ == "__main__":
    l = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    t = 23
    idx = iterative_binary_search(l, t)
    ridx = recursive_binary_search(l, t, 0, len(l) - 1)
    if idx == -1 or ridx == -1:
        print("404")
    else:
        print("Found at", idx, ridx)
