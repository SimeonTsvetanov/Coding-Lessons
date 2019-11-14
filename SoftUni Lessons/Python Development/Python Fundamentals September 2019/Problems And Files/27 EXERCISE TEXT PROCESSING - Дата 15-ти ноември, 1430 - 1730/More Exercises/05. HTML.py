"""
Text Processing - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1741#4

SUPyF2 Text-Pr.-More-Ex. - 05. HTML

Problem:
You will receive 3 lines of input. On the first line you will receive a title of an article.
On the next line you will receive the content of that article.
On the next n lines until you receive "end of comments" you will get the comments about the article.
Print the whole information in html format. The title should be in "h1" tag (<h1></h1>);
the content in article tag (<article></article>); each comment should be in div tag (<div></div>).
For more clarification see the example below

Ecamples:
Input:
SoftUni Article
Some content of the SoftUni article
some comment
more comment
last comment
end of comments

Output:
<h1>
    SoftUni Article
</h1>
<article>
    Some content of the SoftUni article
</article>
<div>
    some comment
</div>
<div>
    more comment
</div>
<div>
    last comment
</div>
"""


def title(text):
    print(f"<h1>\n    {text}\n</h1>")


def article(text):
    print(f"<article>\n    {text}\n</article>")


def comment(text):
    print(f"<div>\n    {text}\n</div>")


def web_site():
    title(input())
    article(input())
    while True:
        text = input()
        if text == "end of comments":
            break
        comment(text)


if __name__ == '__main__':
    web_site()
