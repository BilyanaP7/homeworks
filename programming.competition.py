num_competitors = int(input())
list_points = []

while True:
    for x in range(1, num_competitors + 1):
        name = input()
        points = 0
        while True:
            examiner = input()
            if examiner == "stop":
                break
            else:
                examiner = int(examiner)
                points += examiner
                list_points.append(points)
        print(f"{name} has {points} points.")
        for list_point in list_points:
            if points == max(list_points):
                temp_win = name
                print(f"{name} is the new winner!")
print(f"{temp_win} is the winner!")