my_list = [1, 2, 3, 5, 7]

print("Not Pythonic solution")
for i in my_list:
   print(i, end=" ")

print("\nUnpacking solution")
print(*my_list)