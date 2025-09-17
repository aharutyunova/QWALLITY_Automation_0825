def fibonacci(n1, n2, max_boundary_value):
	sequence = []
	while n1 <= max_boundary_value:
		sequence.append(n1)
		n1, n2 = n2, n1 + n2
	return sequence

