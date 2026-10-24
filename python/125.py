list1 = list(map(int, input(
    "Enter the first list numbers separated by spaces: "
).split()))

list2 = list(map(int, input(
    "Enter the second list numbers separated by spaces: "
).split()))

common = sorted(set(list1) & set(list2))

print("Common elements:", common)