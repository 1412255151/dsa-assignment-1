def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = []

    for num in arr:
        complement = target_sum - num

    
        if complement in seen:
            
            pairs.append((num, complement))

        
        seen.append(num)

    return pairs


input_str = input("Enter integers separated by spaces: ")
arr = list(map(int, input_str.split()))


target_sum = int(input("Enter the target sum: "))

result = find_pairs_with_sum(arr, target_sum)

if result:
    print("Pairs with sum", target_sum, "are:")
    for pair in result:
        print(pair)
else:
    print("No pairs found with sum", target_sum)