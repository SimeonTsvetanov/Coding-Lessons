"""
Technology Fundamentals Retake Final Exam - 20 December 2018
link: https://judge.softuni.bg/Contests/Practice/Index/1394#1
Name: 02. Activation Keys
"""
valid_keys = []
all_keys = input().split("&")
for key in all_keys:
    if key.isalnum() and (len(key) == 16 or len(key) == 25):
        if len(key) == 16:
            key = f"{key[0:4]}-{key[4:8]}-{key[8:12]}-{key[12:16]}".upper()
            key = ''.join([str(9 - int(x)) if x.isdigit() else x for x in key])
        elif len(key) == 25:
            key = f"{key[0:5]}-{key[5:10]}-{key[10:15]}-{key[15:20]}-{key[20:25]}".upper()
            key = ''.join([str(9 - int(x)) if x.isdigit() else x for x in key])
        valid_keys.append(key)

print(", ".join(valid_keys))
