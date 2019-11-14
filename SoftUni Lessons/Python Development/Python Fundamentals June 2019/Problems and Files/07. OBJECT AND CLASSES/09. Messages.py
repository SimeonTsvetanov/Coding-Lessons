"""
Objects and Classes
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/950#8

SUPyF Objects and Classes - 9. Messages *

Problem:
Create a class User, which has a Username (string), and ReceivedMessages (Collection of Messages).
Create a class Message, which has a Content (string) and a Sender (User).
You will have to store a messaging history for every user. The input consists of 2 commands:
“register {username}”
“{senderUsername} send {recipientUsername} {content}”

The register command, registers a user with the given username.
The send command, sends a message, from the given sender, to the given recipient, with the given content.
That means that you must add the message to the recipient’s ReceivedMessages.
If even one of the given names does NOT exist, ignore the command.
When you receive the command “exit” you must end the input sequence. After that you will receive 2 usernames,
separated by a space.
You must print all messages, sent, between the two users, corresponding to the given usernames.
The messages should be printed in a specified way. You should print first a message SENT from the first user,
then a message SENT from the second user, then a message from the first user, and so on.
If one of the collections of messages has more elements than the other, just print the remaining elements from it.
The first user’s messages must be printed in the following way:
“{firstUser}: {content}”
The second user’s message must be printed in the following way:
“{content} :{secondUser}”
When you print the whole output, it should look like this:
{firstUser}: {content1}
{content1} :{secondUser}
{firstUser}: {content2}
{content2} :{secondUser}
. . .
In case there are NO messages between the two users, print “No messages”.

Examples:
    Input:
        register Ivan
        register Pesho
        Ivan send Pesho pesho
        Ivan send Pesho pesho_tam_li_si?
        Pesho send Ivan kaji_vanka
        Pesho send Ivan tuk_sum
        Pesho send Ivan chakai_che_bachkam
        Ivan send Pesho kvo_stava
        Ivan send Pesho kak_si
        Ivan send Pesho deka_izbega_be?
        Ivan send Pesho pecaaa!!!
        exit
        Ivan Pesho
    Output:
        Ivan: pesho
        kaji_vanka :Pesho
        Ivan: pesho_tam_li_si?
        tuk_sum :Pesho
        Ivan: kvo_stava
        chakai_che_bachkam :Pesho
        Ivan: kak_si
        Ivan: deka_izbega_be?
        Ivan: pecaaa!!!
    Input:
        register John
        John send Harry harry_you_there?
        register Harry
        John send Harry harry?
        register Donald
        Harry send John yeah_sorry_was_out...
        Harry send John wassup?
        Donald send John Yo_John?
        Donald send Jonh You_there?
        John send Harry thank_god!!
        John send Harry I_need_you!
        exit
        John Harry
    Output:
        John: harry?
        yeah_sorry_was_out... :Harry
        John: thank_god!!
        wassup? :Harry
        John: I_need_you!
"""
# P.S. I have lost my own solution, of this problem... SO this is copy and paste from someone else's code.


class User:

    def __init__(self, Username, ReceivedMessages):
        self.Username = Username
        self.ReceivedMessages = ReceivedMessages


class Message:

    def __init__(self, Content, Sender):
        self.Content = Content
        self.Sender = Sender


def Max_num(a, b):
    if a > b:
        return a
    else:
        return b


if __name__ == '__main__':

        input_string = input().split(' ')
        users_list = []
        message_list_1 = []
        message_list_2 = []

        while not input_string[0] == 'exit':
            if input_string[0] == 'register':
                newUser = User(input_string[1], [])
                users_list.append(newUser)
            else:

                if input_string[2] in [user.Username for user in users_list] and input_string[0] in [user.Username for user in users_list]:
                    for user in users_list:
                        if user.Username == input_string[2]:
                            newMessage = Message(
                                input_string[3], input_string[0])
                            user.ReceivedMessages.append(newMessage)

            input_string = input().split(' ')

        final_usernames = input().split(' ')

        for user in users_list:
            if user.Username == final_usernames[1]:
                for messages in user.ReceivedMessages:
                    if messages.Sender == final_usernames[0]:
                        message_list_1.append(
                            f'{messages.Sender}: {messages.Content}')

        for user in users_list:
            if user.Username == final_usernames[0]:
                for messages in user.ReceivedMessages:
                    if messages.Sender == final_usernames[1]:
                        message_list_2.append(
                            f'{messages.Content} :{messages.Sender}')

        if len(message_list_1) > 0 or len(message_list_2) > 0:
            for i in range(0, Max_num(len(message_list_1), len(message_list_2))):
                if i < len(message_list_1):
                    print(message_list_1[i])

                if i < len(message_list_2):
                    print(message_list_2[i])
        else:
            print('No messages')