import re

name_pattern = re.compile(r'\b\d+[A-Z][a-z]+?([A-Z\d])\1+\b')

chain_of_responsibility = []

input_lines_count = int(input())
for _ in range(input_lines_count):
	line = input()

	names = list(map(lambda m: m.group(), name_pattern.finditer(line)))

	first_name = names[0]
	last_name = names[-1]

	if len(chain_of_responsibility) >= 2 and first_name != chain_of_responsibility[-1]:
		print('Broke the chain!')
		print(f'Chain: {"->".join(chain_of_responsibility)}')
		exit()

	if len(names) < 2:
		found_pattern = re.compile(name_pattern.pattern + r'.*!!$')
		responsible_match = found_pattern.match(line)

		if responsible_match:
			manager = chain_of_responsibility[-1]
			print(f'Found the manager!: {manager}')
		else:
			print('Did not find the manager!')

		print(f'Chain: {"->".join(chain_of_responsibility)}')
		exit()

	if not chain_of_responsibility:
		chain_of_responsibility.append(first_name)

	chain_of_responsibility.append(last_name)
