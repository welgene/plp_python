# Create an empty list
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Print the original list
#print(f"Original list: {my_list}")

# Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)
#print(my_list)

# Extend the list with another list
my_list.extend([50, 60, 70])
#print(my_list)

# Remove the last element
my_list.pop()
#print(my_list)

# Sort the list in ascending order
my_list.sort()
#print(my_list)

# Find the index of the value 30
index_of_30 = my_list.index(30)

# Print the final list and the index of 30
print(f"Final list: {my_list}")
print(f"Index of 30: {index_of_30}")