# 1. Creating an empty list
my_list = []

# 2. Adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3. Inserting the value 15 at the second position (index 1)
my_list.insert(1, 15)

# 4. Extending my list with [50, 60, 70]
my_list.extend([50, 60, 70])

# 5. Removing the last element
my_list.pop()

# 6. Sorting my list in ascending order
my_list.sort()

# 7. Finding and printing the index of the value 30
index_of_30 = my_list.index(30)
print("List after operations:", my_list)
print("Index of value 30:", index_of_30)
