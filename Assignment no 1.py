
# Sort
list = [9,4,6,11,2]

for i in range(len(list)):
    # unsorted array
    index = i
    for j in range(i + 1, len(list)):
        if list[index] > list[j]:
            index = j
    list[i], list[index] = list[index], list[i]

print("Sorted array")
for i in range(len(list)):
    print(list[i])