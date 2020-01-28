def solve():
    countries = [country for country in input().split(", ")]
    capitals = [capital for capital in input().split(", ")]
    country_with_capitals = zip(countries, capitals)
    [print(f"{country} -> {capital}") for country, capital in country_with_capitals]


if __name__ == '__main__':
    solve()
