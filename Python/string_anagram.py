"""
get length of string
loop from start to middle of string
"""
from string_reverse import reverse_string as reverse

def is_anagram() -> bool:
	s = 'anagram'
	rs = reverse(s)
	len_s = len(s) - 1
	for c in rs:
		if c != s[len_s]:
			return False
		len_s -= 1
	return True

if __name__ == '__main__':
	print(is_anagram())