def reverse_array_in_place(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = input("Enter the array of integers (space-separated): ").split()

arr = [int(num) for num in arr]

reverse_array_in_place(arr)

print("Reversed array:", arr)
