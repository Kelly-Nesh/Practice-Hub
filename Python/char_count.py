"""
loop through string
create a dict
	key = char
	initval = 0
if dict[key] is none
	set to initial value
else
	increment existing value
loop through dict
	get key to highest value
"""


def char_count():
	s = 'increment existing value'
	count = {}
	for c in s:
		if not count.get(c):
			count[c] = 1
		else:
			count[c] += 1
	largest = ''
	current = 0
	for k,v in count.items():
		if v >= current:
			largest = k
			current = v
	return largest

if __name__ == '__main__':
	print(char_count())