rent = int(input())

figures = rent * 0.7
kettering = figures - (figures * 0.15)
sound = kettering / 2

total = figures + kettering + sound + rent

print(f"{total:.2f}")
