toy_size = input("What is the size : ")
toy_color = input("What is the color : ")
num_toys = int(input("How much toys : "))

price = 0

if toy_color == "red":
    if toy_size == "large":
        price += 16
    elif toy_size == "medium":
        price += 13
    elif toy_size == "small":
        price += 9
if toy_color == "green":
    if toy_size == "large":
        price += 12
    elif toy_size == "medium":
        price += 9
    elif toy_size == "small":
        price += 8
if toy_color == "yellow":
    if toy_size == "large":
        price += 9
    elif toy_size == "medium":
        price += 7
    elif toy_size == "small":
        price += 5

toys_price = (price * num_toys) * 0.35
print(f"You have earned {toys_price} leva.")