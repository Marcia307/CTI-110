# Marcia Tyson
# 9/07/2024
# P1HW2
# Create a program that does some basic math on numbers that are entered

print("This Program Claculates and dipsplay trvel expense")
print()
budget_value=int(input("Enter Budget: "))
travel_destination=input("Enter your travel destination: ")
gas=int(input("How much do you think you will spend on gas?: "))
accomodations=int(input("Approximately, how much will you need for accomodations/hotel?: "))
food=int(input("Lastly how much do  you need for food?: "))
print()
print()
print("------------Travel Expenses------------")
print("Location:",travel_destination)
print("Initial Budget", budget_value)
print()
print("Fuel:", gas)
print("Accomodation:", accomodations)
print("Food:", food)
print()
print("Remaining Balance:", budget_value-gas+accomodations+food)
