from collections import deque

ingredients = deque([int(ingredient) for ingredient in input().split()])
freshness = [int(freshness) for freshness in input().split()]

cocktail_recipes = {
    150: "Mimosa",
    250: "Daiquiri",
    300: "Sunshine",
    400: "Mojito"
}

done_cocktails = {
    "Mimosa": 0,
    "Daiquiri":	0,
    "Sunshine":	0,
    "Mojito": 0
}

while ingredients and freshness:

    ingredient = ingredients.popleft()
    if ingredient == 0:
        continue
    fresh = freshness.pop()

    cocktail = ingredient * fresh

    if cocktail in cocktail_recipes:
        done_cocktails[cocktail_recipes[cocktail]] += 1

    else:
        ingredients.append(ingredient + 5)

if any(x == 0 for x in done_cocktails.values()):
    print("What a pity! You didn't manage to prepare all cocktails.")
else:
    print("It's party time! The cocktails are ready!")
if ingredients:
    print(f"Ingredients left: {sum(ingredients)}")
for cocktail, count in sorted(done_cocktails.items()):
    if count > 0:
        print(f" # {cocktail} --> {count}")
