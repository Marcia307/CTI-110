# Marcia Tyson
# 9/07/2024
# P1HW2
# Create a program that does some basic math on numbers that are entered

print("This Program Claculates and dipsplay trvel expense")
print()
budget_value=int(input("Enter Budget: "))
print()
travel_destination=input("Enter your travel destination: ")
print()
gas_value=int(input("How much do you think you will spend on gas?: "))
print()
accomodations_value=int(input("Approximately, how much will you need for accomodations/hotel?: "))
print()
food_value=int(input("Lastly how much do  you need for food?: "))
print()
print("------------Travel Expenses------------")
print("Location:",travel_destination)
print("Initial Budget", budget_value)
print()
print("Fuel:", gas_value)
print("Accomodation:", accomodations_value)
print("Food:", food_value)
print()
print("Remaining Balance:", budget_value-gas_value-accomodations_value-food_value)
