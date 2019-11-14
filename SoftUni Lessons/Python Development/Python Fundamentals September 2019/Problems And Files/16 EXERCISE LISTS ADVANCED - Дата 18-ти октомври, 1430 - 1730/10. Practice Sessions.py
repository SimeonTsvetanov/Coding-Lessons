"""
Lists Advanced - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1731#8

SUPyF2 Lists-Advanced-Exercise - 10. Practice Sessions (not included in final score)

Problem:
The racers must practice for the race. Your job is to keep the records of the roads and the time for each lap.
The track with the best time will be the chosen one for the finals.

Write a program, that keeps information about roads and the racers who practice on them.
When the practice begins, you’re going to start receiving data until you get the "END" message.
There are three possible commands:
•	"Add->{road}->{racer}"
o	Add the road if it doesn't exist in your collection and add the racer to it.
•	"Move->{currentRoad}->{racer}->{nextRoad}"
o	Find the racer on the current road and move him to the next one, only if he exists in the current road.
    Both roads will always be valid and will already exist.
•	"Close->{road}"
o	Find the road and remove it from the sessions, along with the racers on it if it exists.
In the end, print all of the roads with the racers who have practiced and ordered by the count of the racers in
descending order, then by the roads in ascending order. The output must be in the following format:
Practice sessions:
{road}
++{racer}
++{racer}
++{racer}
………………………..
Input / Constraints
•	You will be receiving lines of information in the format described above, until you receive the "END" command.
•	The input will always be in the right format.
•	Both roads from the "Move" command will always be valid and you don't need to check them explicitly.
Output
•	Print the roads with their racers in the format described above

Examples:
Input:
Add->Glencrutchery Road->Giacomo Agostini
Add->Braddan->Geoff Duke
Add->Peel road->Mike Hailwood
Add->Glencrutchery Road->Guy Martin
Move->Glencrutchery Road->Giacomo Agostini->Peel road
Close->Braddan
END

Output:
Practice sessions:
Peel road
++Mike Hailwood
++Giacomo Agostini
Glencrutchery Road
++Guy Martin

Comments:
We add racers to the roads they are racing on. When we receive the "Move" command,
we check if Giacomo Agostini is on Glencrutchery Road and if he is,
we remove him from it and add him to the next one - Peel road.
When we receive the "Close" command, we remove Brandon road and remove all its records.
In the end we print the roads sorted by the count of racers on them and then by the
names of the roads in ascending order.
"""
all_roads = []

while True:
    data = input().split("->")
    if data[0] == "END":
        break
    elif data[0] == "Add":
        trace_in_all_roads = False
        for trace in all_roads:
            if trace[0] == data[1]:
                trace_in_all_roads = True
                trace += [data[2]]
                break
        if not trace_in_all_roads:
            all_roads += [[data[1], data[2]]]
    elif data[0] == "Move":
        for trace in all_roads:
            if trace[0] == data[1]:
                if data[2] in trace:
                    trace.remove(data[2])
                    for trace_2 in all_roads:
                        if trace_2[0] == data[3]:
                            trace_2 += [data[2]]
    elif data[0] == "Close":
        for trace in all_roads:
            if trace[0] == data[1]:
                all_roads.remove(trace)

all_roads = sorted(sorted(all_roads, key=lambda x: x[0]), key=lambda x: len(x), reverse=True)

print("Practice sessions:")
for road in all_roads:
    print(road[0])
    for driver in road[1:]:
        print(f"++{driver}")

