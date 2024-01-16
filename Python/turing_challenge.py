#!/usr/bin/env python3
"""
Decode string to number
Example
input s = "$@@@"
output = 13

Symbol  Value
@       1
#       5
$       10
%       50
&       100
+       500
~       1000

Constraints:
    1 <= length(s) <= 10
    s contains only the above characters
    it is guaranteed that s is a valid roman numeral in the range [10, 3999]
"""
import unittest


def decode(s: str) -> int:
    sym = {"@": 1, "#": 5, "$": 10, "%": 50, "&": 100, "+": 500, "~": 1000}
    val = 0
    j = len(s) - 1
    for idx, itm in enumerate(s):
        cur = sym[itm]
        if idx >= j:
            if cur >= sym[s[idx - 1]]:
                val += cur
            else:
                 val -= cur
            continue
        nxt = sym[s[idx + 1]]
        if cur >= nxt:
            val += cur
        else:
            val -= cur
    return val


class Test_decode(unittest.TestCase):
        str1 = "$@@@"
        str2 = "%~"
        str3 = "&#%"
        str4 = "~&+$%@#"
        str5 = "~~&&$$@@"
        str6 = "~&&$$$@#"
        str7 = "+%$#@@@"

        def test_str1(self):
            self.assertEqual(decode(self.str1), 13)
        def test_str2(self):
            self.assertEqual(decode(self.str2), 950)
        def test_str3(self):
            self.assertEqual(decode(self.str3), 145)
        def test_str4(self):
            self.assertEqual(decode(self.str4), 1444)
        def test_str5(self):
            self.assertEqual(decode(self.str5), 2222)
        def test_str6(self):
            self.assertEqual(decode(self.str6), 1234)
        def test_str7(self):
            self.assertEqual(decode(self.str7), 568)
