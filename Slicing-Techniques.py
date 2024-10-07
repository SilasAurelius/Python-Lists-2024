temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Task 1: Extract the temperatures for the second week (7 days) of the month(index 7 to index 14):
print(temperatures[7:14])

# Had to redo the slice because I had it original set to [8:15]

# Task 2: Extract the temperatures above 100.
print(temperatures[23:])

#Though using a for loop to iterate over the list and using a >= 100 operator worked, I wanted to simplify the code. I used print(len(temperatures)) to quickly find that there are 30 items in the list. Then I counted backwards from 30 to the first 100, then used my slice from that point. In hindsight, I could have used get().