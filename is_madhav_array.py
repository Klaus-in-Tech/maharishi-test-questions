"""
 A Madhav array has the following property.
a[0] = a[1] + a[2] = a[3] + a[4] + a[5] = a[6] + a[7] + a[8] + a[9] = ...
The length of a Madhav array must be n*(n+1)/2 for some n.
Write a method named isMadhavArray that returns 1 if its array argument is a Madhav array,
otherwise it returns 0. If you are programming in Java or C# the function signature is
int isMadhavArray(int[] a)

Examples
 -----------------------------------|-------|---------------------------------------------------
| if a is                           | return| reason                                            |
|-----------------------------------|-------|---------------------------------------------------|
| {2,1,1}                           | 1     | 2 = 1 + 1                                         |
|-----------------------------------|-------|---------------------------------------------------|
| {2,1,1,4,-1,-1}                   | 1     | 2 = 1 + 1, 2 = 4 + -1 + -1                        |
|-----------------------------------|-------|---------------------------------------------------|
| {6,2,4,2,2,2,1,5,0,0}             | 1     | 6 = 2 + 4, 6 = 2 + 2 + 2, 6 = 1 + 5 + 0 + 0       |
|-----------------------------------|-------|---------------------------------------------------|
| {18,9,10,6,6,6}                   | 0     | 18 != 9 + 10                                      |
|-----------------------------------|-------|---------------------------------------------------|
| {-6,-3,-3,8,-5,-4}                | 0     | -6 != 8 + -5 + -4                                 |
|-----------------------------------|-------|---------------------------------------------------|
| {0,0,0,0,0,0,0,0,0,0,1,1,1,-2,-1} | 1     | 0 = 0+0, 0 = 0+0+0, 0 = 0+0+0+0, 0 = 1+1+1+-2+-1  |
|-----------------------------------|-------|---------------------------------------------------|
| {3,1,2,3,0}                       | 0     | The length of the array is 5, but 5 != n*(n+1)/2  |
 -----------------------------------|-------|---------------------------------------------------
"""

#Input an array 
#Output integer 

def is_madhav_array(arr):
    if not arr:
        return 0
    length = len(arr)
    
    n = 1 
    while n*(n+1)//2< length:
        n+=1
    if n*(n+1)//2 != length:
        return 0
        
    target_sum = arr[0]
    index =1 
    group_size = 2
    
    while index<length:
        group_sum = sum(arr[index:index+group_size])
        if group_sum != target_sum:
            return 0
        index+=group_size
        group_size+=1
            
    return 1
   
   
print(is_madhav_array([2,1,1])) # return 1
print(is_madhav_array([2,1,1,4,-1,-1])) # return 1
print(is_madhav_array([6,2,4,2,2,2,1,5,0,0])) # return 1
print(is_madhav_array([18,9,10,6,6,6])) # return 0
print(is_madhav_array([-6,-3,-3,8,-5,-4])) # return 0
print(is_madhav_array([0,0,0,0,0,0,0,0,0,0,1,1,1,-2,-1])) # return 1
print(is_madhav_array([3,1,2,3,0])) # return 0

