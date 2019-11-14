"""
Objects and Classes
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/950#4

SUPyF Objects and Classes - 05. Optimized Banking System

Problem:
Create a class BankAccount which has a Name (string), Bank (string) and Balance (decimal).
You will receive several input lines, containing information in the following way:
{bank} | {accountName} | {accountBalance}
You need to store every given Account. When you receive the command “end” you must stop the input sequence.
Then you must print all Accounts, ordered by their balance, in descending order, and then by length of the bank name,
in ascending order.
The accounts must be printed in the following way “{accountName} -> {balance} ({bank})”.
Note: Numbers must be printed rounded to the 2nd decimal digit.

Examples:
----------------------------------------------------------------------------------------------
    Input:                          |   Output:
----------------------------------------------------------------------------------------------
DSK | Ivan | 504.403                |Aleksander -> 20000.00 (DSK)
DSK | Pesho | 2000.4031             |Aleksander -> 20000.00 (Piraeus)
DSK | Aleksander | 20000.0001       |Pesho -> 2000.40 (DSK)
Piraeus | Ivan | 504.403            |Ivan -> 504.40 (DSK)
Piraeus | Aleksander | 20000.0001   |Ivan -> 504.40 (Piraeus)
end                                 |
----------------------------------------------------------------------------------------------
"""


class BankAccount:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance


all_accounts = []

while True:
    command = input()
    if command == "end":
        break
    d = [item for item in command.split(" | ")]
    account = BankAccount(d[1], d[0], float(d[2]))
    all_accounts += [account]

all_accounts = sorted(sorted(all_accounts, key=lambda x: x.bank), key=lambda x: x.balance, reverse=True)

for account in all_accounts:
    print(f"{account.name} -> {account.balance:.2f} ({account.bank})")

