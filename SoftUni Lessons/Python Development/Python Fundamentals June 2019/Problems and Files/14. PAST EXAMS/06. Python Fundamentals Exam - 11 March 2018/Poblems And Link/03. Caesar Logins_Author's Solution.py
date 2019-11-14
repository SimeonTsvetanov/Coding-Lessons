import re


def get_shift_character_length(_str):
	snipped_string = _str[1:-1]
	non_alphanumeric_chars = re.findall(r'[^a-zA-Z\d]', snipped_string)

	shift_length = len(non_alphanumeric_chars)
	return shift_length


def caesar_shift(_str, shift_count):
	shifted_chars = [chr(ord(c) - shift_count) for c in _str]
	result = ''.join(shifted_chars)
	return result


pattern = re.compile(
	r'^([/\\])[^a-zA-Z\d]*?([a-zA-Z\d]+)[^a-zA-Z\d]*?\2[^a-zA-Z\d]*?([a-zA-Z\d]+)[^a-zA-Z\d]*?\3[^a-zA-Z\d]*?\2[^a-zA-Z\d]*?\3[^a-zA-Z\d]*?\1$')

while True:
	line = input()
	if line == '/end/':
		break

	match = pattern.match(line)

	if not match:
		continue

	user, password = match.group(2), match.group(3)

	shift_chars = get_shift_character_length(line)

	shifted_user = caesar_shift(user, shift_chars)
	shifted_pass = caesar_shift(password, shift_chars)

	print(f'user: {shifted_user}, pass: {shifted_pass}')
