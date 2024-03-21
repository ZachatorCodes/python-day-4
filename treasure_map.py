line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# Solution 1
row_letter = position[0]
row_number = int(position[1]) - 1

if row_letter == "A":
  map[row_number][0] = "X"
elif row_letter == "B":
  map[row_number][1] = "X"
else:
  map[row_number][2] = "X"
#Solution 2
letter = position[0]
abc = ["A", "B", "C"]
# Finds the index of a certain value
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")