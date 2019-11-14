exam_hour = int(input())
exam_minute = int(input())
actual_hour = int(input())
actual_minute = int(input())

exam_time = (exam_hour * 60) + exam_minute

actual_time = (actual_hour * 60) + actual_minute

difference_time = (abs(actual_time - exam_time))
difference_hour = difference_time // 60
difference_minute = difference_time % 60

difference_early = exam_time - 30

if actual_time == exam_time:
    print("On time")
elif actual_time >= difference_early and actual_time < exam_time:
    print("On time")
    print(f"{difference_minute} minutes before the start")
elif actual_time < difference_early:
    if difference_time < 60:
        print("Early")
        print(f"{difference_minute} minutes before the start")
    else:
        if difference_minute < 10:
            print("Early")
            print(f"{difference_hour}:0{difference_minute} hours before the start")
        else:
            print("Early")
            print(f"{difference_hour}:{difference_minute} hours before the start")
elif actual_time > exam_time:
    if difference_time < 60:
        print("Late")
        print(f"{difference_minute} minutes after the start")
    else:
        if difference_minute < 10:
            print("Late")
            print(f"{difference_hour}:0{difference_minute} hours after the start")
        else:
            print("Late")
            print(f"{difference_hour}:{difference_minute} hours after the start")




