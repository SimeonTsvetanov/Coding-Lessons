import operator

state_integers = list(map(int, input().split(' ')))
command_integers = list(map(int, input().split(' ')))

for integer in command_integers:
	mul_or_div = operator.mul if integer % 2 == 0 else operator.floordiv

	parity = 0 if abs(integer) % 2 == 0 else 1
	state_integers = [mul_or_div(num, abs(integer)) if num % 2 == parity else num for num in state_integers]

	filter_sign = lambda num: num < 0 if integer < 0 else num > 0
	state_integers = [num + integer if filter_sign(num) else num for num in state_integers]

print(state_integers)
