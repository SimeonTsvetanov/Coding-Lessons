"""
Dictionaries - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1737#9

SUPyF2 Dict-Exercise - 10. SoftUni Exam Results (not included in final score)

Problem:
Judge statistics on the last Programing Fundamentals exam was not working correctly, so you have the task to take all the submissions and analyze them properly. You should collect all the submissions and print the final results and statistics about each language that the participants submitted their solutions in.
You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished". You should store each username and his submissions and points.
You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that case, you should remove the user from the contest, but preserve his submissions in the total count of submissions for each language.
After receiving "exam finished" print each of the participants, ordered descending by their max points, then by username, in the following format:
Results:
{username} | {points}
…
After that print each language, used in the exam, ordered descending by total submission count and then by language name, in the following format:
Submissions:
{language} – {submissionsCount}
…
Input / Constraints
Until you receive "exam finished" you will be receiving participant submissions in the following format:
"{username}-{language}-{points}".
You can receive a ban command -> "{username}-banned"
The points of the participant will always be a valid integer in the range [0-100];
Output
•	Print the exam results for each participant, ordered descending by max points and then by username,
in the following format:
Results:
{username} | {points}
…
•	After that print each language, ordered descending by total submissions and then by language name,
in the following format:
Submissions:
{language} – {submissionsCount}
…
•	Allowed working time / memory: 100ms / 16MB.
Examples:
Input:
Pesho-Java-84
Gosho-C#-84
Gosho-C#-70
Kiro-C#-94
exam finished

Output:
Results:
Kiro | 94
Gosho | 84
Pesho | 84
Submissions:
C# - 3
Java - 1

Comment:
We order the participant descending by max points and then by name, printing only the username and the max points.
After that we print each language along with the count of submissions,
ordered descending by submissions count, and then by language name.

Input:
Pesho-Java-91
Gosho-C#-84
Kiro-Java-90
Kiro-C#-50
Kiro-banned
exam finished

Output:
Results:
Pesho | 91
Gosho | 84
Submissions:
C# - 2
Java - 2

Comment:
Kiro is banned so he is removed from the contest, but
he`s submissions are still preserved in the languages submissions count.
So althou there are only 2 participants in the results, there are 4 submissions in total.
"""

# ---------------------------------------------------------------------------------------------
# I have created two solutions to this problem. First will be with Dictionaries:
# ---------------------------------------------------------------------------------------------

"""
submissions = {}
submissions_count = {}

while True:
    command = input()
    if command == "exam finished":
        break
    data = command.split("-")
    if len(data) == 3:  # Adding new submission.
        username = data[0]
        language = data[1]
        points = int(data[2])
        # If we don't have such user:
        if username not in submissions:
            submissions[username] = [language, points]
        # if we have him
        else:
            # check if the new points are more then the old submission.
            if submissions[username][1] < points and language == submissions[username][0]:
                submissions[username][1] = points

        # Check if we have the language in the submissions_count
        if language in submissions_count:
            submissions_count[language] += 1
        else:  # If we don't have it:
            submissions_count[language] = 1

    elif len(data) == 2:  # Banning user.
        user_to_ban = data[0]
        if user_to_ban in submissions:
            submissions.pop(user_to_ban)

# Print all the results:
print(f"Results:")
for user, value in sorted(submissions.items(), key=lambda x: (-x[1][1], x[0])):
    print(f"{user} | {value[1]}")

print(f"Submissions:")
for language, count in sorted(submissions_count.items(), key=lambda x: (-x[1], x[0])):
    print(f"{language} - {count}")
"""

# ---------------------------------------------------------------------------------------------
# And the second will be with Objects and Classes:
# ---------------------------------------------------------------------------------------------


class Submissions:
    all_users = []
    submissions = {}

    def __init__(self, username, language, points):
        self.username = username
        self.language = language
        self.points = int(points)
        self.add_or_update_user()
        self.add_or_update_submission()

    @classmethod
    def run(cls):
        while True:
            submission = input()
            if submission == "exam finished":
                Submissions.print()
                break
            submission = submission.split("-")
            if len(submission) == 3:
                Submissions(submission[0], submission[1], int(submission[2]))
            else:
                Submissions.banned(submission[0])

    def add_or_update_user(self):
        add_new_user = True
        for user in Submissions.all_users:
            if user.username == self.username:
                add_new_user = False
                if self.points > user.points:
                    user.points = self.points
        if add_new_user:
            Submissions.all_users += [self]

    def add_or_update_submission(self):
        if self.language not in Submissions.submissions:
            Submissions.submissions[self.language] = 1
        else:
            Submissions.submissions[self.language] += 1

    @classmethod
    def print(cls):
        print("Results:")
        for user in sorted(Submissions.all_users, key=lambda p: (-p.points, p.username)):
            print(f"{user.username} | {user.points}")
        print(f"Submissions:")
        for language, count in sorted(Submissions.submissions.items(), key=lambda x: (-x[1], x[0])):
            print(f"{language} - {count}")

    @classmethod
    def banned(cls, name):
        for user in Submissions.all_users:
            if user.username == name:
                Submissions.all_users.remove(user)


if __name__ == '__main__':
    Submissions.run()


