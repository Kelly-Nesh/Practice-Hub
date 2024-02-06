"""
get length of string
loop from end back to beginning
concatenate string
"""

def reverse_string() -> str:
	s = 'qwerty'
	strlen = len(s) - 1
	rev_str = ''
	while strlen >= 0:
		rev_str += s[strlen]
		strlen -= 1
	return rev_str

if __name__ == '__main__':
	print(reverse_string())