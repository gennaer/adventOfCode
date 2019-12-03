
def compFuel(mass):
	return int(mass)//3-2

def adjustFuel(orig_fuel):
	add_fuel = compFuel(orig_fuel)
	adjusted_fuel = 0
	while add_fuel>0:
		adjusted_fuel += add_fuel
		add_fuel = compFuel(add_fuel)

	return orig_fuel + adjusted_fuel


file = open('input.txt','r')
#d = file.readline()
#print(int(d)//3-2)
fuel_total = 0
adj_fuel_total = 0
for line in file:
	module_fuel = compFuel(line)
	adj_module_fuel = adjustFuel(module_fuel)
	fuel_total += module_fuel
	adj_fuel_total += adj_module_fuel
#    print(line)
print(fuel_total)
print(adj_fuel_total)