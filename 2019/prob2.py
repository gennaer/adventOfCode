
codes = []
with open('input_p2.txt','r') as f:
	d = f.readline().split(',') # assuming just one line
	for opcode in d:
		codes.append(int(opcode)) 

# make adjustments as required by problem:
codes[1] = 12
codes[2] = 2
orig_code = codes.copy() # for alternate way of doing problem

# here's one way to do this: break into chunks of 4
from itertools import zip_longest
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

for opc, c1, c2, p in grouper(codes, 4):
	if opc == 99:
		break
	elif opc == 1:
		codes[p] = codes[c1]+codes[c2]
	elif opc == 2:
		codes[p] = codes[c1]*codes[c2]
	else:
		print('Uh Oh') # not doing a nice exception here because lazy

print(codes[0])

# ok after reading part 2, that's probably not what they intended
# let's try a different way:
def execute_code(intcode):
	inst_ptr = 0
	inst_end = False
	while not inst_end:
		opc = intcode[inst_ptr]
		p1 = intcode[inst_ptr+1]
		p2 = intcode[inst_ptr+2]
		p3 = intcode[inst_ptr+3]
		if opc == 99:
			inst_end = True
			continue
		elif opc == 1:
			intcode[p3] = intcode[p1]+intcode[p2]
		elif opc == 2:
			intcode[p3] = intcode[p1]*intcode[p2]
		inst_ptr += 4
	return intcode[0]

codes2 = orig_code.copy()
print(execute_code(codes2))



# now let's try part 2:
target = 19690720
param_found = False
for noun in range(100):
	for verb in range(100):
		test_code = orig_code.copy()
		test_code[1] = noun
		test_code[2] = verb
		if execute_code(test_code) == target:
			param_found = True
			break
	if param_found:
		break

print(100*noun+verb)