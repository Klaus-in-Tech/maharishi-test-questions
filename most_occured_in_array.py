"""
Write a function that will return the most occurring number in an array. If there is more than
one such number, the function may return any one of them.
If you are programming in Java or C#, the function signature is int answerTwo(int[] a)

Examples
 -------------------------|----------|------------------------------------------------------------
| a                       | return   | Explanation                                                |
|-------------------------|----------|------------------------------------------------------------|
| {6,8,1,8,2}             | 8        | 8 occurs two times. No other number occurs 3 or more times |
|-------------------------|----------|------------------------------------------------------------|
| {6,8,1,8,6}             | 8 or 6   | 8, 6. The Function may return either 8 or 6                |
 -------------------------|----------|------------------------------------------------------------
"""

#Input an array 
#Output string 

from collections import Counter


def answerTwo(arr):
    if not arr:
        return None
    
    counter = Counter(arr)
    return f"{counter.most_common(1)[0][0]} occurs two times." 
   
 
print(answerTwo([6,8,1,8,2]))
print(answerTwo([6,8,1,8,6]))
