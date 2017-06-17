def validate_string(s):
	
	r = [False, False, False, False, False] # initialize to 0s then set True or False after iterating through s

	for c in s:
		if str.isalnum(c): r[0] = True
		if str.isalpha(c): r[1] = True
		if str.isdigit(c): r[2] = True
		if str.islower(c): r[3] = True
		if str.isupper(c): r[4] = True

	return r




if __name__ == "__main__":
	s = raw_input()
	r = validate_string(s)

	for b in r:
		print b