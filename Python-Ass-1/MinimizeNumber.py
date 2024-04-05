def max_operations(N, A):
    # Initialize the counter for the operations
    operations = 0

    # Continue until all numbers are even
    while all(a % 2 == 0 for a in A):
        # Divide all numbers by 2
        A = [a // 2 for a in A]
        # Increment the operation counter
        operations += 1

    return operations

def main():
    # Read N from standard input
    N = int(input().strip())
    # Read the array A from standard input
    A = list(map(int, input().strip().split()))
    # Calculate and print the maximum possible number of operations
    print(max_operations(N, A))

if __name__ == "__main__":
    main()
