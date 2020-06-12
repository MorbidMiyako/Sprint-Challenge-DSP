import time

start_time = time.time()

# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

# duplicates = []  # Return the list of duplicates in this data structure

# # # Replace the nested for loops below with your improvements
# # # Original for loop doesnt find duplicates in own file!!! hence the difference between slow faulty for loop and MVP + Stretch solution

# # for name_1 in names_1:
# #     for name_2 in names_2:
# #         if name_1 == name_2:
# #             duplicates.append(name_1)

# class BSTNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.count = 1

#     # Insert the given value into the tree
#     def insert(self, value):
#         if value < self.value:
#             if self.left is None:
#                 self.left = BSTNode(value)
#             else:
#                 self.left.insert(value)
#         elif value > self.value:
#             if self.right is None:
#                 self.right = BSTNode(value)
#             else:
#                 self.right.insert(value)
#         elif value == self.value and self.count == 1:
#             duplicates.append(value)
#             self.count += 1


# name_tree = BSTNode("L")
# for name_1 in names_1:
#     name_tree.insert(name_1)
# for name_2 in names_2:
#     name_tree.insert(name_2)


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

f1 = open('names_1.txt', 'r')
f2 = open('names_2.txt', 'r')
names = f1.read().split("\n")
names.extend(f2.read().split("\n"))
names.sort()
f1.close()
f2.close()

duplicate_free = list(set(names))
# Return the list of duplicates in this data structure
for name in duplicate_free:
    duplicates = names.remove(name)

# index_number = 0
# while index_number < len(names) - 1:
#     if names[index_number] == names[index_number + 1]:
#         duplicates.append(names[index_number])
#         index_number += 2
#     else:
#         index_number += 1

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
