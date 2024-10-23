line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

#grab hold of the first letter that is in the input 
#turn it into a lowercase to compare it with a comparable 
letter = position[0].lower()
abc = ["a", "b", "c"]
#doing a comparison that comes from python list called index
#finding the index in our abc list 
letter_index = abc.index(letter)
#getting hold of the number index 
number_index = int(position[1]) - 1
#bring up our nested listy and put in both of these, remember for nested list
# we go from outside to in that i why letter index is to the right 
map[number_index][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
