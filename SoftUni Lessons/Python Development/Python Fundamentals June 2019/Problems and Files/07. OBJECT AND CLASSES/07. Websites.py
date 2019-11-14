"""
Objects and Classes
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/950#6

SUPyF Objects and Classes - 07. Websites

Problem:
You have been tasked to create an ordered database of websites. For the task you will need to create a class Website,
which will have a Host, a Domain and Queries.
The Host and the Domain are simple strings.
The Queries, is Collections of strings.
You will be given several input lines in the following format:
{host} | {domain} | {query1,query2. . .}
Note: There will always be a host and a domain, but there might NOT be ANY queries.
The input sequence ends, when you receive the command “end”. Then you must print all websites in the following format:
https://www.{host}.{domain}/query?=[{query1]&[{query2}]&[query3]. . .
In case there are NO queries, just print:
https://www.{host}.{domain}

Examples:

INPUT:
    softuni | bg | user,course,homework
    judge.softuni | bg | contest,bg
    google | bg | search,query
    zamunda | net
    end
OUTPUT:
    https://www.softuni.bg/query?=[user]&[course]&[homework]
    https://www.judge.softuni.bg/query?=[contest]&[bg]
    https://www.google.bg/query?=[search]&[query]
    https://www.zamunda.net
"""


class Website:
    def __init__(self, host, domain, queries):
        self.host = host
        self.domain = domain
        self.queries = queries


web_addresses = []

while True:
    inp = input()
    if inp == "end":
        break
    data = [item for item in inp.split(" | ")]
    if len(data) > 2:
        queries_ = [item for item in data[2].split(",")]
        web_address = Website(host=data[0], domain=data[1], queries=queries_)
        web_addresses += [web_address]
    else:
        queries_ = "Nope"
        web_address = Website(host=data[0], domain=data[1], queries=queries_)
        web_addresses += [web_address]

for item in web_addresses:
    if item.queries != "Nope":
        print(f"https://www.{item.host}.{item.domain}/query?=", end="")
        counter = 1
        for query in item.queries:
            if counter < len(item.queries):
                print(f"[{query}]&", end="")
                counter += 1
            else:
                print(f"[{query}]")
    else:
        print(f"https://www.{item.host}.{item.domain}")
