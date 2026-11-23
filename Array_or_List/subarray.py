# Create a method to find the longest increasing subarray in an array of integers.

list1 = [2, 3, 5, 1, 6, 2, 1]

current_count = 1
max_count = 1
start_index = 0

for i in range(len(list1) - 1):

    if list1[i] < list1[i + 1]:
        current_count += 1

        if current_count > max_count:
            max_count = current_count
            start_index = i + 1 - current_count + 1

    else:
        current_count = 1

longest_array = list1[start_index : start_index + max_count]

print("Longest increasing subarray:", longest_array)
print("Length:", max_count)