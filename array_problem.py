"""
Write a function that will return 1 if an integer array satisfies the following conditions and returns 0 otherwise.
1. it has even numbers of elements
2. Sum of all the numbers in the first half of the array is equal to the sum of all the numbers in the second half of the array.

If you are programming in Java, the function Signature is
int answerThree(int[] a)
Examples
 -------------------|--------|-----------------------------------------------------------------------
| a                 | return | Explanation                                                           |
|-------------------|--------|-----------------------------------------------------------------------|
| {5,4,3,2,3,4,6,1} | 1      | *There are 8 (even) number of elements in the array. Thus condition 1 |
|                   |        | satisfied.                                                            |
|                   |        | *The sum of all the numbers in the first half = 5+4+3+2 = 14          |
 -------------------|--------|-----------------------------------------------------------------------
"""

#Input an array 
#Output string 

def answerThree(arr):
    length_of_arr = len(arr)
    middle_index = length_of_arr//2
    sum_of_first_half = sum(arr[:middle_index])
    sum_of_last_half = sum(arr[middle_index:])
 
    if (sum_of_first_half == sum_of_last_half) and len(arr)%2 == 0:
        return 1
    else:
        return 0
        
print(answerThree([5,4,3,2,3,4,6,1]))
