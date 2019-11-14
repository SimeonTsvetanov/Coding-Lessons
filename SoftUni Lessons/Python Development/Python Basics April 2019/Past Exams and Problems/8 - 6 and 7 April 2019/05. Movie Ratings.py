import sys

count_movies = int(input())

max_rated_movie = -sys.maxsize - 1
min_rated_movie = sys.maxsize
max_rated_name = None
min_rated_name = None
total_rating = 0

for movie in range(count_movies):
    name = input()
    rating = float(input())
    total_rating += rating
    if rating > max_rated_movie:
        max_rated_movie = rating
        max_rated_name = name
    if rating < min_rated_movie:
        min_rated_movie = rating
        min_rated_name = name

print(f"{max_rated_name} is with highest rating: {max_rated_movie:.1f}")
print(f"{min_rated_name} is with lowest rating: {min_rated_movie:.1f}")
print(f"Average rating: {(total_rating / count_movies):.1f}")
