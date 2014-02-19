import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
"w", "x", "y", "z"]
num = range(0, 10)
let_output = []
output = []
answers = ["yes", "no"]
answer = " "
result = " "
num_count = " "
letter_count = " "
upper_count = " "
password = " "
def sep(s, n):
  print s * n
def ask():
	global answer
	global answers
	while answer.lower() not in answers:
		answer = raw_input("Do You Wish To Write Your Password To a File Called 'password.txt'? ")
		if answer not in answers:
			print "Please Clarify Your Input."
sep(" ", 1)
sep("-", 50)
while type(num_count) != int:
	try:
		num_count = int(raw_input("How Many Numbers?"))
		if not num_count >= 0:
			num_count = " "
			print "Amount of Numbers Must Be Greater Than Or Equal to 0."
	except ValueError:
		None
while type(letter_count) != int or type(upper_count) != int or not letter_count >= 0 or not upper_count >= 0:
	try:
		letter_count = int(raw_input("How Many Letters?"))
		upper_count = int(raw_input("How many Upper-case letters?"))
		if not letter_count >= 0:
			letter_count = " "
			print "Amount of Letters Must Be Greater Than Or Equal to 0."
		elif not upper_count >= 0:
			upper_count = " "
			print "Amount of Upper-Case Letters Must Be Greater Than Or Equal to 0."
		elif not upper_count <= letter_count:
			upper_count = " "
			print "Amount of Upper-Case Letters Must Be Less Than Or Equal to Amount of Letters."
	except ValueError:
		None
sep("-", 50)
sep(" ", 1)
for i in range(num_count):
	new_num = random.choice(num)
	output.append(new_num)
for i in range(letter_count):
	new_let = random.choice(letters)
	let_output.append(new_let)
for i in range(upper_count):
	up_let = random.choice(let_output)
	let_output.remove(up_let)
	up_let = up_let.upper()
	output.append(up_let)
for i in let_output:
	output.append(i)
for i in range(3):
	random.shuffle(output)
for i in output:
	result += str(i)
result = result[1::]
sep("=", 50)
print "Your Password Is: %s" % result
sep("=", 50)
sep(" ", 1)
ask()
if answer.lower() == answers[0]:
	with open("password.txt", "a") as my_file:
		my_file.write(str(result) + "\n")
	print """
	File Written.
	"""
else:
	sep(" ", 1)