"""
Consider the positive integer 50. Note that 50 = 25 + 25 = 5^2 + 5^2 and 50 = 1 + 49 = 1^2 + 7^2,
Thus 50 can be expressed as a sum of the two squares in two different ways.
Write a method whether or not a positive integer n can be expressed as a sum of two squares in
exactly two different ways.
The signature of the function is
int answerOne(int n)
"""

import math


def answerOne(n):
    if n<0:
        return 0
    expressions = []
    for a in range(int(math.sqrt(n)+1)):
        a_squared = a**2
        b_squared = n-a_squared
        
        b = int(math.sqrt(b_squared))
        if b**2 == b_squared:
            if a<=b:
                expressions.append((a,b))
    return expressions if len(expressions) == 2 else 0
        
    

# Test the function
print(f"answerOne(50): {answerOne(50)}")  # Should return 1
print(f"answerOne(25): {answerOne(25)}")  # Should return 1 (0^2 + 5^2, 3^2 + 4^2)
print(f"answerOne(5): {answerOne(5)}")    # Should return 1 (1^2 + 2^2)
print(f"answerOne(10): {answerOne(10)}")  # Should return 1 (1^2 + 3^2)
print(f"answerOne(1): {answerOne(1)}")    # Should return 0 (only 0^2 + 1^2)
print(f"answerOne(2): {answerOne(2)}") 
