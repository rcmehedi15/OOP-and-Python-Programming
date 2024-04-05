def min_removals_to_good_sequence(a):
    count = {}
    for num in a:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    removals = 0
    for num, occurrences in count.items():
        if occurrences > num:
            removals += occurrences - num  # Remove excess occurrences
        elif occurrences < num:
            removals += occurrences  # Remove all occurrences of this number
    
    return removals

# Input processing
N = int(input().strip())
a = list(map(int, input().strip().split()))

# Calculating and printing the result
print(min_removals_to_good_sequence(a))
