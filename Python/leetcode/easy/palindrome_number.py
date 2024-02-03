#!/usr/bin/python3
"""
Checks if an integer is a palindrome

My approach. Convert to string first
Submission link
-> https://leetcode.com/problems/palindrome-number/submissions/1164701169

Time taken: 7 m 33 s
"""
import unittest


def is_palindrome(x: int) -> list:
    x = str(x)
    end = len(x) - 1
    st = 0
    while st <= end:
        if x[st] == x[end]:
            st += 1
            end -= 1
        else:
            return False
    return True


class TestIsPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome(5445))
        self.assertFalse(is_palindrome(-5445))
        self.assertTrue(is_palindrome(22))
        self.assertFalse(is_palindrome(994949))


if __name__ == "__main__":
    print("run as unittest")
