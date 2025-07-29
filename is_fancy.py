"""
A fancy number is a number in the sequence 1,1,5,17,61,... Note the first two fancy numbers
are 1 and any fancy number other than the first two is sum of three times previous one and two times
the one before that. see below
1,
1,
3*1 + 2*1 = 5,
5*3 + 2*1 = 17,
17*3 + 5*2 = 61
Write a function named is_fancy that returns 1, if it's integer argument is a Fancy number,
otherwise it returns 0.
"""

def is_fancy(n):
    if n == 1:
        return 1
    prev = 1
    p_perv = 1
    
    while True:
       current_num = 3*prev + 2*p_perv
       if current_num == n:
           return 1
       elif current_num > n:
           return 0
       
       p_perv = prev
       prev = current_num
        
        
# Test the function with fancy numbers
print(f"is_fancy(1): {is_fancy(1)}")    # Should return 1
print(f"is_fancy(5): {is_fancy(5)}")    # Should return 1
print(f"is_fancy(17): {is_fancy(17)}")  # Should return 1
print(f"is_fancy(61): {is_fancy(61)}")  # Should return 1
print(f"is_fancy(10): {is_fancy(10)}") 