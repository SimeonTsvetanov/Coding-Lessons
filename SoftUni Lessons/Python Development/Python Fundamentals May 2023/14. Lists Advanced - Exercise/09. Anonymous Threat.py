# TODO - the divide case is not done yet.

# input_line = [x for x in input().split(' ')]
#
# while True:
#     command = input().split(' ')
#     if command[0] == "3:1":
#         break
#     elif command[0] == "merge":
#
#         start_index = int(command[1])
#         end_index = int(command[2])
#
#         if start_index < 0:
#             start_index = 0
#         if end_index >= len(input_line):
#             end_index = len(input_line) -1
#
#         merged = ''.join(input_line[start_index: end_index + 1])
#         input_line = input_line[:start_index] + input_line[end_index + 1:]
#
#         input_line.insert(start_index, merged)
#
#     elif command[0] == "divide":
#
# print(' '.join(input_line))