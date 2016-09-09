#Compute relative error for array u:
from numpy import array, zeros, log10, linspace, exp, size, subtract, shape, resize




def find_error(filename):
	with open(filename) as infile:
		infile.readline()
		line = infile.readline()
		lines = line.split()
		#n = int(lines[1].replace("=", ""))
		print lines
		n = int(lines[2])
		u = zeros((n+1,))
		#infile.readline()
		i = 0
		for line in infile:
			u[i] = float(line)
			i += 1
	x = linspace(0, 1, n+1)
	exact_sol = 1 - (1 - exp(-10))*x - exp(-10*x)
	print exact_sol
	#error = log(abs(u - exact_sol)) - log(abs(exact_sol))
	error = log10(abs(subtract(u, exact_sol)))#/exact_sol))
	#print u.shape, error.shape, exact_sol.shape, x.shape
	print error
	#print abs(u - exact_sol)/abs(exact_sol)
	return error

find_error("Nmodtest.txt")





