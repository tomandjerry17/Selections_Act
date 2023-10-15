# Prompts the user to enter
year = eval(input("Year of birth? \n\t: "))
print()

# Formula
sign = year % 12

# Display
if sign == 0:
    print(str(year) + " is the year of the Monkey")
elif sign == 1:
    print(str(year) + " is the year of the Rooster")
elif sign == 2:
    print(str(year) + " is the year of the Dog")
elif sign == 3:
    print(str(year) + " is the year of the Pig")
elif sign == 4:
    print(str(year) + " is the year of the Rat")
elif sign == 5:
    print(str(year) + " is the year of the Ox")
elif sign == 6:
    print(str(year) + " is the year of the Tiger")
elif sign == 7:
    print(str(year) + " is the year of the Rabbit")
elif sign == 8:
    print(str(year) + " is the year of the Dragon")
elif sign == 9:
    print(str(year) + " is the year of the Snake")
elif sign == 10:
    print(str(year) + " is the year of the Horse")
elif sign == 11:
    print(str(year) + " is the year of the Sheep")
