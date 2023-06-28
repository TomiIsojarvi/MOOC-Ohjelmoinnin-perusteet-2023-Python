###############################################################################
# get_value - Either get a value from a variable or return an integer
###############################################################################
def get_value(vars:dict, value: str):
	if value in vars:
		return vars[value]
	else:
		return int(value)

###############################################################################
# arithmetics - Arithmetic-operations
###############################################################################
def arithmetics(parts: list, vars: dict):
		arg = 0
		var = parts[1]

		# Check if the second argument is a variable or an integer.
		arg = get_value(vars, parts[2])

		# MOV #############################
		if parts[0] == "MOV":
				vars[var] = arg

		# ADD #############################
		if parts[0] == "ADD":
				vars[var] += arg

		# SUB #############################
		if parts[0] == "SUB":
				vars[var] -= arg

		# MUL #############################
		if parts[0] == "MUL":
				vars[var] *= arg
		
###############################################################################
# condtion - Check a condition
###############################################################################
def condition(arg1, condition, arg2):
	if condition == "==":
		return arg1 == arg2
	if condition == "!=":
		return arg1 != arg2
	if condition == "<":
		return arg1 < arg2
	if condition == "<=":
		return arg1 <= arg2
	if condition == ">":
		return arg1 > arg2
	if condition == ">=":
		return arg1 >= arg2


###############################################################################
# suorita - Executes the code
###############################################################################
def suorita(code: list) -> list:

	# SEYUP ###################################################################

	# Program Counter
	prog_count = 0

	# Setup all the variables to zero.
	vars = dict.fromkeys(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',\
		'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 0)
	
	# Number of lines of code
	lines = len(code)

	# Jump locations
	jump_list = {}

	# Prints
	prints = []

	# No code... Return an empty list.
	if lines == 0:
		return code

	# CREATE THE JUMP LIST ####################################################

	for row in range(0, lines):
		line = code[row]
		parts = line.split()

		if parts[0].endswith(":"):
			parts[0] = parts[0].strip(":")
			jump_list[parts[0]] = row

	# MAIN LOOP ###############################################################

	while True:
			# End of Code... Stop... 
			if prog_count == len(code):
				break

			# Currently executed line and opcode (operation code).
			line = code[prog_count]
			line = line.split()
			opcode = line[0]

			# A jump.location... Continue...
			if opcode.endswith(":"):
				prog_count += 1
				continue

			# OPCODES #########################################################

			# END ###########################
			if opcode == "END":
				break

			# PRINT #########################
			if opcode == "PRINT":
				arg = get_value(vars, line[1])
				prints.append(arg)

			# MOV, ADD, SUB & MUL ###########
			if opcode == "MOV" or opcode == "ADD" or opcode == "SUB" or opcode == "MUL":
				arithmetics(line, vars)

			# JUMP ##########################
			if opcode == "JUMP":
				jump = line[1]

				if jump in jump_list:
					prog_count = jump_list[jump]

			# IF ############################
			if opcode == "IF":
				arg1 = get_value(vars, line[1])
				arg2 = get_value(vars, line[3])
				cond = line[2]
				jump = prog_count
				
				# Check condition
				if condition(arg1, cond, arg2):
					jump = line[5]

				if jump in jump_list:
					prog_count = jump_list[jump]

			prog_count += 1
		
	return prints


if __name__ == "__main__":
	ohjelma4 = []
	ohjelma4.append("MOV N 50")
	ohjelma4.append("PRINT 2")
	ohjelma4.append("MOV A 3")
	ohjelma4.append("alku:")
	ohjelma4.append("MOV B 2")
	ohjelma4.append("MOV Z 0")
	ohjelma4.append("testi:")
	ohjelma4.append("MOV C B")
	ohjelma4.append("uusi:")
	ohjelma4.append("IF C == A JUMP virhe")
	ohjelma4.append("IF C > A JUMP ohi")
	ohjelma4.append("ADD C B")
	ohjelma4.append("JUMP uusi")
	ohjelma4.append("virhe:")
	ohjelma4.append("MOV Z 1")
	ohjelma4.append("JUMP ohi2")
	ohjelma4.append("ohi:")
	ohjelma4.append("ADD B 1")
	ohjelma4.append("IF B < A JUMP testi")
	ohjelma4.append("ohi2:")
	ohjelma4.append("IF Z == 1 JUMP ohi3")
	ohjelma4.append("PRINT A")
	ohjelma4.append("ohi3:")
	ohjelma4.append("ADD A 1")
	ohjelma4.append("IF A <= N JUMP alku")
	tulos = suorita(ohjelma4)
	print(tulos)