def rotx(input, amt):
	"""	Variant of the ROT13 substitution cipher that can rotate by any amount 1-26. 
		Takes in an string, and an integer rotate amt"""
	lows = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	CAPS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	rotated = ""
	for i in input:
		if i in lows:
			rotated += lows[(lows.index(i)+amt) % 26]
		elif i in CAPS:
			rotated += CAPS[(CAPS.index(i)+amt) % 26]
		else:
			rotated += i 
	return rotated