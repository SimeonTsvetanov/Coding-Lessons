import math
name = input()
count_seasons = int(input())
count_episodes = int(input())
time_episode = float(input())

adverts = time_episode * 0.2
time_episode = time_episode + adverts
added_special_time = count_seasons * 10
total = (time_episode * count_episodes * count_seasons) + added_special_time

print(f"Total time needed to watch the {name} series is {math.floor(total)} minutes.")
