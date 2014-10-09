"""
The function fixedPointIteration() computes approximate solution of g(x) = x.
It takes a single-variable function G, starting guess X_0, and number of
iteration steps K, and returns an approximate solution. 
"""
def fixedPointIteration(g, x_0, k):
	"""
	>>> fixedPointIteration(lambda x: 1.0 - x**3, 0.5, 12)
	0.0
	>>> fixedPointIteration(lambda x: 1.0 - x, 0.5, 20)
	0.5
	"""
	x = []
	x.append(x_0)
	for i in range(k):
		x.append(g(x[i]))
	return x[k];

if __name__ == "__main__":
    import doctest
    doctest.testmod()
