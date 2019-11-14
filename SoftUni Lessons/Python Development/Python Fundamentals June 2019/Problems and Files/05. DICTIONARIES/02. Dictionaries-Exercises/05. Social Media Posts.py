"""
Dictionaries - Exercises
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1088#4

SUPyF Dictionaries Exercises - 05. Social Media Posts

Problem:
You have been tasked to create a Console Social Media Database.
You will receive several input lines in one of the following formats:
- post {postName}
- like {postName}
- dislike {postName}
- comment {postName} {commenterName} {content}
If you receive the post command, you must create a post with the given name.
If you receive the like command you must add a like to the given post.
If you receive the dislike command you must add a dislike to the given post.
If you receive the comment command, you must add a comment to the given post.
The comment’s writer must be the given commentator name, and the content of the comment must be the given content.
By default, the posts have 0 likes, 0 dislikes and 0 comments when created.
When you receive the command “drop the media”, you must end the input sequence, and you must print every post with its
likes, dislikes and comments in the following format:
Post: {postName} | Likes: {likes} | Dislikes {dislikes}
Comments:
*  {commentator1}: {comment1}
*  {commentator2}: {comment2}
. . .
If a certain post does not have any comments, you should just print “None”.
The comments have a prefix of a single asterisk (‘*’) and 2 spaces.
There is NO space between the commentator’s name and the colon.
Constraints
- The post name will be a string of letters and digits.
- The commentator’s name will be a string of letters.
- The comment’s CONTENT, may contain ANY ASCII character.
- There will be NO invalid input data.
EXAMPLES:
    INPUT <<<
post FirstPost
like FirstPost
like FirstPost
dislike FirstPost
post SecondPost
comment FirstPost Isacc Cool
comment SecondPost Isacc Lol
like SecondPost
drop the media
    OUTPUT >>>
Post: FirstPost | Likes: 2 | Dislikes: 1
Comments:
*  Isacc: Cool
Post: SecondPost | Likes: 1 | Dislikes: 0
Comments:
*  Isacc: Lol

    INPUT <<<
post SomePost
like SomePost
like SomePost
dislike SomePost
post OtherPost
comment OtherPost Isacc Naaais
comment OtherPost Peter GoodPost
comment OtherPost John Meh...
drop the media
    OUTPUT >>>
Post: SomePost | Likes: 2 | Dislikes: 1
Comments:
None
Post: OtherPost | Likes: 0 | Dislikes: 0
Comments:
*  Isacc: Naaais
*  Peter: GoodPost
*  John: Meh...
"""
social_media = {}

while True:
    command = input()
    if command == "drop the media":
        break
    a = [word for word in command.split(" ")]
    if a[0] == "post":
        social_media[a[1]] = {}
        social_media[a[1]]["Likes"] = 0
        social_media[a[1]]["Dislikes"] = 0
        social_media[a[1]]["Comments"] = {}
    elif a[0] == "like":
        social_media[a[1]]["Likes"] += 1
    elif a[0] == "dislike":
        social_media[a[1]]["Dislikes"] += 1
    elif a[0] == "comment":
        if a[1] in social_media:
            social_media[a[1]]["Comments"][a[2]] = a[3:]
        elif a[1] not in social_media:
            social_media[a[1]]["Comments"][a[2]] += a[3:]

for post, key, in social_media.items():
    print(f"Post: {post} | ", end="")

    for value in key:
        if value == "Likes":
            print(f"{value}: {key[value]} | ", end="")
        elif value == "Dislikes":
            print(f"{value}: {key[value]}")
        elif value == "Comments":
            if len(key[value]) == 0:
                print("Comments:")
                print("None")
            else:
                print("Comments:")
                for val in key[value]:
                    print(f"*  {val}: ", end="")
                    print(" ".join(key[value][val]))
