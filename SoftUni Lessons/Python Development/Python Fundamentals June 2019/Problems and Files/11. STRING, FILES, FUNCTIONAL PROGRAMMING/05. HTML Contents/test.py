with open("txt_file.txt", "r") as file:
    line = file.readline()
    title_content = "HTML-Contents"
    first_part = f"<!DOCTYPE html>\n<html>\n<head>\n\t<title>{title_content}</title>\n</head>\n<body>"
    second_part = ""
    third_part = f"</body>\n</html>"

    while not line == "exit\n":
        tag, content = line.split()
        if tag == "title":
            title_content = content
        else:
            opening_tag = f"\t<{tag}>"
            closed_tag = f"</{tag}>\n"
            row = f"{opening_tag}{content}{closed_tag}"
            second_part += row
        line = file.readline()


with open("html_file.html", "a") as html_file:
    html_file.write(first_part)
    html_file.write(second_part)
    html_file.write(third_part)

