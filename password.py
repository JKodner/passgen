def generate(num, lett, uplet, directory=False):
	"""Generates a password with the given parameter options.

	There are 3 parameters that can account to the way the password is generated:

	The 'num' value is the number of randomly chosen numbers that will be present in the password, 
	the 'lett' value is the number of randomly chosen letters that will be present in the password, 
	and the 'uplet' value is the number of letters that would be capitalized.

	Note: The 'uplet' value cannot be greater than the 'lett' value, or else an error will be
	raised.

	There is also an optional 'directory' parameter that allows the password to be written to a
	file. The file-name in the directory must be existing, or else an IOError will be raised."""
	from random import (choice, shuffle)
	from string import lowercase
	keys = {num: "Num", lett: "Lett", uplet: "Uplet"}
	for i in keys.keys():
		if not isinstance(i, int) or not i >= 0:
			raise ValueError("'%s' value is not positive integer." % keys[i])
		if keys[i] == "Uplet":
			if uplet > lett:
				raise ValueError("'Uplet' value is greater than 'lett' value.")
	output = []
	letters = [i for i in lowercase]
	for i in range(lett):
		chosen = choice(letters)
		output.append(chosen)
	for i in range(uplet):
		chosen = ""
		while not chosen.islower():
			chosen = choice(output)
		new_let = chosen.upper()
		output[output.index(chosen)] = new_let
	for i in range(num):
		chosen = choice(range(10))
		output.append(str(chosen))
	for i in range(3):
		shuffle(output)
	output = ''.join(output)
	if isinstance(directory, str):
		from os import path
		if path.exists(directory):
			with open(directory, "w") as f:
				f.write(output + "\n")
		else:
			raise IOError("Given 'directory' value is not valid directory.")
	else:
		return output