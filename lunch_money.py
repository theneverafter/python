from decimal import *
# TODO: figure out why .prec includes leading digits
getcontext().prec = 4

lunch_price = 2.95

def findCost(days, price, balance):
    cost = days * Decimal(price) - Decimal(balance)
    return cost


print("-" * 41)
print("Welcome to Josh's Lunch Money Calculator!")
print("-" * 41)

jayden_balance = float(input("Enter Jayden's remaining balance: "))
levi_balance = float(input("Enter Levi's remaining balance: "))

print(f"Is the cost of a lunch still {lunch_price}?")

# TODO: add input error handling 
same_price = input("Yes / No: ")

if same_price.lower() == "no":
    lunch_price = Decimal(input("Enter the new lunch price: "))

school_days = int(input("How many school days in this period?: "))

jayden_cost = findCost(school_days, lunch_price, jayden_balance)
levi_cost = findCost(school_days, lunch_price, levi_balance)
total_cost = jayden_cost + levi_cost

print("-" * 41)
print(f"""Thanks! For this school period:

Jayden needs: ${jayden_cost}
Levi needs:   ${levi_cost}
Total cost:   ${total_cost}""")
print("-" * 41)
