square_feet= input("Enter number of square feet: ")
one_acre= 43560
square_feet = int(square_feet)
acres = square_feet / one_acre
remaining_feet = square_feet % one_acre
whole_acres = int(acres)

print(square_feet, " square feet is ", format(acres, ".2f"), " acres ")
print(square_feet, "square feet is", whole_acres, "whole acres(s) with", remaining_feet, " square feet remaining")
