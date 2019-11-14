time_for_movie = int(input())
count_scenes = int(input())
time_one_scene = int(input())

preparation = time_for_movie * 0.15
time_all_scenes = count_scenes * time_one_scene
needed_time = preparation + time_all_scenes

if time_for_movie >= needed_time:
    print(f"You managed to finish the movie on time! You have {round(time_for_movie - needed_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(needed_time - time_for_movie)} minutes.")
