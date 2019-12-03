
def compFuel(mass):
	''' compute fuel required for a given mass'''
	return int(mass)//3-2

def adjustFuel(orig_fuel):
	''' compute additional fuel required to haul base (orig) fuel '''
	add_fuel = compFuel(orig_fuel)
	adjusted_fuel = 0
	while add_fuel>0:
		adjusted_fuel += add_fuel
		add_fuel = compFuel(add_fuel)

	return orig_fuel + adjusted_fuel

fuel_total = 0
adj_fuel_total = 0
# read in the input file
with open('input.txt','r') as f:
	for line in f:
		module_fuel = compFuel(line)
		adj_module_fuel = adjustFuel(module_fuel)
		fuel_total += module_fuel
		adj_fuel_total += adj_module_fuel
#    print(line)
print(fuel_total)
print(adj_fuel_total)