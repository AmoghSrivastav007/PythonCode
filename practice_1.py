'''
Problem Statement -

A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array  of N number of integer values. The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).

Example 1 :

N=8 and arr = [4,5,0,1,9,0,5,0].

There are 3 empty packets in the given set. These 3 empty packets represented as O should be pushed towards the end of the array

Input :

8  - Value of N

[4,5,0,1,9,0,5,0] - Element of arr[O] to arr[N-1],While input each element is separated by newline

Output:

4 5 1 9 5 0 0 0

Example 2:

Input:

6 — Value of N.

[6,0,1,8,0,2] - Element of arr[0] to arr[N-1], While input each element is separated by newline

Output:

6 1 8 2 0 0
'''


def move_zeroes_to_end(arr):
    # Initialize a pointer for the position of the next non-zero element
    non_zero_index = 0

    # Iterate through the array
    for i in range(len(arr)):
        # If the current element is not zero, move it to the non-zero index
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1

    # Fill the remaining elements with zeroes
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0

    return arr
# Read input values
N = int(input("Enter the number of packets (N): "))
print("Enter the elements of the array (one per line):")
arr = [int(input()) for _ in range(N)]
# Move zeroes to the end and print the result
result = move_zeroes_to_end(arr)
print("Output:")
print(' '.join(map(str, result)))
