def read_file(filename):
	lines = []
	with open(filename, 'r' , encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert_file(lines):
	new = []
	person = None
	for line in lines:
		if line == 'John':
			person = line
			continue
		elif line == 'Zak':
			person = line
			continue
		if person:
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert_file(lines)
	write_file('output.txt', lines)

main()