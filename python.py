# print("Hello world")



# num = int(input("Enter a number: "))

# if num < 0:
#     print("The number is negative.")
# elif num == 0:
#     print("The number is zero.")
# else:
#     print("The number is positive.")

# for i in range(1, 6):
#     print(f"Square of {i} is {i ** 2}")


fruits = ["apple", "banana", "cherry", "date"]

print("Original list:", fruits)

fruits.append("grape")
fruits.insert(1, "kiwi")
fruits.remove("cherry")

print("Modified list:", fruits)

for fruit in fruits:
    print(fruit.upper())

sorted_fruits = sorted(fruits)
print("Sorted list:", sorted_fruits)
