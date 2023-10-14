dog_food = int(input())

while True:
    daily_food = input()
    if daily_food != "stop":
        daily_food = int(daily_food)
        leftover = (dog_food * 1000) - daily_food
        needed_food = daily_food - (dog_food * 1000)
    else:
        break

if daily_food:
    daily_food = int(daily_food)   
    if daily_food > dog_food:
        print(f"Food is not enough.You need {needed_food} grams more.")
    elif daily_food < dog_food:
        print(f"Food is enough! Leftovers : {leftover} grams.")
    else:
        print("Food is enough! There is none left.")

print(f"So you spent {dog_food * 5.50} leva for food.")