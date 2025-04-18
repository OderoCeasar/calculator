# Lists
my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)  

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from my_list
my_list.pop() 

# Sort my_list in ascending order
my_list.sort()

# Step 7: Find and print the index of the value 30 in my_list
index = my_list.index(30)
print("Index of 30:", index)

# Optional: Print the final state of my_list
print("Final my_list:", my_list)