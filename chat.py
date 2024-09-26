def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: #if suffer some strange symbol in the beginning, need to add '-sig' to remove it.
		for line in f:
			lines.append(line.strip())
	return lines

def convert(Lines):
	new = []
	person = None  #Claim person to prevent code hang on if the first words in the input.txt are not Allen
	for line in Lines:
		print(line)
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	print(new)	
	return(new)

def write_file(filename, Lines):
	with open(filename, 'w') as f:
		for line in Lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	print(lines)
	lines = convert(lines)
	write_file('output.txt', lines)

main()



