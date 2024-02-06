"""
Change str to lowercase.
have a list/str of vowels
check if letter is a vowel
	if true, increment vowel
	continue
	else if consonant
	if true, increment consonant
return vowel, consonant count
"""


def vowel_consonant_count():
	s = 'vowel_consonant_count'
	vowels = 'aeiou'
	vowel_count = 0
	consonant_count = 0

	for l in s:
		if l in vowels:
			vowel_count += 1
		elif l >= 'a' and l <= 'z':
			consonant_count += 1

	return vowel_count, consonant_count

if __name__ == '__main__':
	print(vowel_consonant_count())