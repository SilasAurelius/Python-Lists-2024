# Task 1: Given two lists, find out if Alice submitted their assignment and attended class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

print("Alice" in submitted and "Alice" in attended)
# This did not work at first because I needed to specify to look for "Alice in submitted" and look for "Alice" in attend. Simply used and without typing "Alice" in both conditions of the line would result in a false positive.

