import numpy as np
import re

# part 1
inpt = '234208-765869'

def parse_input(inpt):
	'''return the range of possible pwds from the string input'''
	inp_range = inpt.split('-')
	return (int(inp_range[0]), int(inp_range[1]))

def check_pwd(pwd):
	digit_diff = np.diff([int(i) for i in str(pwd)])
	return np.all(digit_diff>=0) and np.any(digit_diff==0)

#check: 
assert(check_pwd(111111))
assert(not check_pwd(223450))
assert(not check_pwd(123789))

inp_range = parse_input(inpt)

pwd_count = 0
for pwd in range(inp_range[0],inp_range[1]+1):
	if check_pwd(pwd):
		pwd_count+=1

print(pwd_count)
# there's probably a faster, more clever way of doing this...

# part 2:
# idea: in the diff sequence, look for one zero with no nonzero next to it:

def check_pwd2(pwd):
	digit_diff = np.diff([int(i) for i in str(pwd)])
	diff_str = ''.join(str(d) for d in digit_diff)
	single_match = re.search( '(^0[^0])|([^0]0[^0])|([^0]0$)',diff_str)
	return np.all(digit_diff>=0) and np.any(digit_diff==0) and single_match

pwd_count = 0
for pwd in range(inp_range[0],inp_range[1]+1):
	if check_pwd2(pwd):
		pwd_count+=1

print(pwd_count)