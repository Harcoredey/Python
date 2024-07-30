word = input("Enter your word: ")
vowels = ' '
consonants = ' '
for character in word:
	if character in ['a','e', 'i', 'o', 'u']:
		if character.lower():
			vowels += character
		else:
			consonant += character
print(f"the no of vowels is {len(set(vowels))}\n the no of consonants is {len(set(consonants))}")


#name = input("enter name: ")
#if name = a, e, i, o, u: 
#	number = vowel
#if name = b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, #y, z:

#print(f there are ' ' vowels and ' ' consonant)