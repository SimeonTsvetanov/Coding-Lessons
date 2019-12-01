"""
Exam Preparation Programming Fundamentals Final Exam Retake - 9 August 2019
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1767#2
Name: Followers

Problem:
Now that Pesho has successfully created an account, he wants to connect with other users and gain as many followers,
likes and comments as possible.
Create a program that keeps information about Pesho's followers, likes and comments. Keep a record of the followers,
each with the likes and comments Pesho has received from them.
You will be receiving lines with commands until you receive the "Log out" command.  There are four possible commands:
•	"New follower: {username}":
o	Add the username, to your records (with 0 likes and 0 comments).
If person with the given username already exists ignore the line.
•	"Like: {username}: {count}":
o	If the username doesn't exist, add it to your records with the given count of likes.
o	If the username exist, increase the count of likes with the given count.
•	"Comment: {username}":
o	If the username doesn't exist, add it to your records with 1 comment.
o	If the username exists, increase the count of commens with 1.
•	"Blocked: {username}":
o	Delete all records of the given username. If it doesn’t exist, print:
 "{Username} doesn't exist."

In the end, you have to print the count of followers, each follower with his/her likes and comments
(the sum of likes and comments)
sorted in descending order by the likes and then by their username in ascending order in the following format:
{count} followers
{username}: {likes+comments}
{username}: {likes+comments}
...
Input
•	You will be receiving lines until you receive the "Log out" command.
•	The input will always be valid.
Output
•	Print the users with their likes in the format described above.
Examples:
Input:
New follower: gosho
Like: gosho: 5
Comment: gosho
New follower: gosho
New follower: tosho
Comment: gosho
Comment: tosho
Comment: pesho
Log out

Output:
3 followers
gosho: 7
pesho: 1
tosho: 1

Input:
Like: A: 3
Comment: A
New follower: B
Blocked: A
Comment: B
Like: C: 5
Like: D: 5
Log out

Output:
3 followers
C: 5
D: 5
B: 1
"""
