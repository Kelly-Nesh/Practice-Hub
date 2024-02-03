"""Converts a roman numeral to an integer
Submission:
-> https://leetcode.com/problems/roman-to-integer/submissions/1164716195
Time taken: 9 m 0 s
"""
import unittest

def romanToInt(s: str) -> int:
    roman = {
        'I': 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    dec = 0
    end = len(s)
    for i, j in enumerate(s):
        if i + 1 == end or roman[j] >= roman[s[i + 1]]:
            dec += roman[j]
        else:
            dec -= roman[j]
    return dec


class TestRomanToInt(unittest.TestCase):
    def test1(self):
        self.assertEqual(romanToInt("III"), 3)
    def test2(self):
        self.assertEqual(romanToInt("LVIII"), 58)
    def test3(self):
        self.assertEqual(romanToInt("MCMXCIV"), 1994)
    def test4(self):
        self.assertEqual(romanToInt("MMXXIV"), 2024)


if __name__ == "__main__":
    print("run as unittest")
