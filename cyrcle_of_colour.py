user_points=0

num_rotation = int(input())

red = 0
orange = 0
yellow = 0
white = 0
black = 0
other_color = 0

for i in range(0, num_rotation):
    user_guess = input()
    
    if user_guess == "red":
        user_points += 5
        red += 1
    elif user_guess == "orange":
        user_points += 10
        orange += 1
    elif user_guess == "yellow":
        user_points += 15
        yellow += 1
    elif user_guess == "white":
        user_points += 20
        white += 1
    elif user_guess == "black":
        user_points//2
        black += 1
    else:
        other_color += 1

print(f"Total points: {user_points}")
print(f"Red sector: {red}")
print(f"Orange sector: {orange}")
print(f"Yellow sector: {yellow}")
print(f"White sector: {white}")
print(f"Other colors picked: {other_color}")
print(f"Divides from black: {black}")