
codes = []
with open('input.txt','r') as f:
	d = f.readline().split(',') # assuming just one line
	for opcode in d:
		# for alternate way of doing this below
		codes.append(int(opcode)) 

# make adjustments as required by problem:
codes[1] = 12
codes[2] = 2

# alternate way by breaking apart into chunks of 4:
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