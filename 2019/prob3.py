wires = []
with open('input_p3.txt','r') as f:
	for lines in f:
		wires.append(lines.split(','))

# really dumb, memory-inefficient, Matlab-y way that does not scale
# the much saner way is to store only the coordinates of visited locations
# e.g. as a set or list and then compare them for matches (intersection)
# across wires

import numpy as np
grid = np.zeros((len(wires),25001,25001), dtype=np.int)

grid_cent_r = 12500
grid_cent_c = 12500
w = 0
for wire in wires:
	start_r = grid_cent_r
	start_c = grid_cent_c
	end_r = grid_cent_r
	end_c = grid_cent_c
	for move in wire:
		move_dir = move[0]
		move_amt = int(move[1:])
		if move_dir == 'R':
			end_c = start_c + move_amt
			grid[w,start_r,start_c+1:end_c+1] = 1
			start_c = end_c
		elif move_dir == 'L':
			end_c = start_c - move_amt
			grid[w,start_r,end_c:start_c] = 1
			start_c = end_c
		elif move_dir == 'U':
			end_r = start_r - move_amt
			grid[w,end_r:start_r,start_c] = 1
			start_r = end_r
		elif move_dir == 'D':
			end_r = start_r + move_amt
			grid[w,start_r+1:end_r+1,start_c] = 1
			start_r = end_r
	w += 1

grid = np.sum(grid,axis=0)

# find closest intersection
intersects = np.unravel_index(np.where(grid.ravel()>1),grid.shape)
nInts = len(intersects[0][0])
intersects = [[intersects[0][0][x],intersects[1][0][x]] for x in range(nInts)]
min_dist = 1e6
for intersect in intersects:
	int_dist = abs(intersect[0]-grid_cent_r) + abs(intersect[1]-grid_cent_c)
	if int_dist < min_dist:
		min_dist = int_dist

print(min_dist)
# this is right, but not great

# again, a really dumb way of doing this for part 2: numbering the steps
#wires = [['D3','R3'],['R3','D3']]
grid = np.zeros((len(wires),25001,25001), dtype=np.int)

grid_cent_r = 12500
grid_cent_c = 12500
w = 0
for wire in wires:
	start_r = grid_cent_r
	start_c = grid_cent_c
	end_r = grid_cent_r
	end_c = grid_cent_c
	startVal = 1
	for move in wire:
		move_dir = move[0]
		move_amt = int(move[1:])
		endVal = startVal+move_amt-1
		if move_dir == 'R':
			end_c = start_c + move_amt
			grid[w,start_r,start_c+1:end_c+1] = np.arange(startVal,endVal+1)
			start_c = end_c
		elif move_dir == 'L':
			end_c = start_c - move_amt
			grid[w,start_r,end_c:start_c] = np.arange(endVal,startVal-1,-1)
			start_c = end_c
		elif move_dir == 'U':
			end_r = start_r - move_amt
			grid[w,end_r:start_r,start_c] = np.arange(endVal,startVal-1,-1)
			start_r = end_r
		elif move_dir == 'D':
			end_r = start_r + move_amt
			grid[w,start_r+1:end_r+1,start_c] = np.arange(startVal,endVal+1)
			start_r = end_r
		startVal = endVal+1
	w += 1

grid = np.sum(grid,axis=0)

intSteps = [grid[isect[0],isect[1]] for isect in intersects]
print(np.min(intSteps))