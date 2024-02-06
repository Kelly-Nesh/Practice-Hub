"""
get length of string
loop from start to middle of string
"""


def is_palindrome() -> bool:
	# s = 'racecar'
	s = 'racer'
	# s = 'mom'
	r = len(s) - 1
	l = 0
	while l <= r:
		if s[l] == s[r]:
			l += 1
			r -= 1
		else:
			return False
	return True

if __name__ == '__main__':
	print(is_palindrome())