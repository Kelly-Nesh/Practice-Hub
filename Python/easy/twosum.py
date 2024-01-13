#!/usr/bin/env python3
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
import unittest


class TwoSum:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """return indices of the two numbers such that they add up to
        target."""
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if (nums[i] + nums[j]) is target:
                    return [i, j]


class TestTwoSum(unittest.TestCase):
    list1 = [1, 2, 3,4,5]
    target1 = 1
    list2 = [2,7,11,15]
    target2 = 9
    list3 = [3,2,4]
    target3 = 6
    list4 = [3,3]
    target4 = 6

    def setUp(self):
        self.ts = TwoSum().twoSum

    def test_none(self):
        result = self.ts(self.list1, self.target1)
        self.assertIsNone(result)

    def test_empty_list(self):
        self.assertEqual(self.ts([], 0), None)

    def test_found(self):
        self.assertEqual(self.ts(self.list2, self.target2), [0, 1])
        self.assertEqual(self.ts(self.list3, self.target3), [1, 2])
        self.assertEqual(self.ts(self.list4, self.target4), [0, 1])
