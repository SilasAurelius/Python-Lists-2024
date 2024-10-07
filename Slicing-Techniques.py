temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Task 1: Extract the temperatures for the second week (7 days) of the month(index 7 to index 14):
print(temperatures[7:14])

# Had to redo the slice because I had it original set to [8:15]

# Task 2: Extract the temperatures above 100.
"""temp_100_and_above = []

for temp in temperatures[20:]:
    if temp >= 100:
        temp_100_and_above.append(temp)
        print(temp_100_and_above)
# Used a for loop to iterate ove the list and then a if statement to append each individual item 100 or above to my new empty list.
"""

print(temperatures[23:])

# I could have just did a simple slice of:
# print(t)