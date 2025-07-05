
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
    


print("\n***** YOUR CART *****") 
for food in foods:
    print(food, end=" ")

total = sum(prices) 
print(f"\nYour total is R{total}")  