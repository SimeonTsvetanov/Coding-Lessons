def loading_bar(percent):
    result = ''

    if percent == 100:
        result = f"100% Complete!\n[%%%%%%%%%%]"
    else:
        result = f"{percent}% [{(int(percent / 10)) * '%'}{(10 - (int(percent / 10))) * '.'}]\nStill loading..."

    return result


print(loading_bar(int(input())))
