"""
An array with an odd number of elements is said to be centered if all elements (except the middle one) are strictly greater than the value of the middle element. Note that only arrays with an odd number of elements have a middle element. Write a function that accepts an integer array and returns 1 if it is a centered array, otherwise it returns 0.
Examples:

if the input array is	return
{1, 2, 3, 4, 5}	0 (the middle element 3 is not strictly less than all other elements)
{3, 2, 1, 4, 5}	1 (the middle element 1 is strictly less than all other elements)
{3, 2, 1, 4, 1}	0 (the middle element 1 is not strictly less than all other elements)
{1, 2, 3, 4}	0 (no middle element)
{}	0 (no middle element)
{10}	1 (the middle element 10 is strictly less than all other elements)
"""

def centered_array_checker(arr):
    length = len(arr)
    middle_index = length // 2
    if not arr:
        return[]
    if length%2 == 0:
        return 0
    for index in range(length):
        if index != middle_index and arr[middle_index] >= arr[index]:
            return 0
    return 1


print(centered_array_checker([1, 2, 3, 4, 5]))
print(centered_array_checker([3, 2, 1, 4, 5]))
print(centered_array_checker([3, 2, 1, 4, 1]))
print(centered_array_checker([1, 2, 3, 4]))
print(centered_array_checker([]))