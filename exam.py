"""
Q1.

Define a function named convert_numbers that:
1. declares a string parameter,
2. converts the string parameter to use strings instread of numbers,
3. and returns the converted string

You may not use regular expressions in any way.

Hint: you can't modify strings, but you can add to them.

E.g:
 9 -> nine
 High 5 -> High five
 2 the moon -> two the moon
 Hang 10 -> Hang onezero

 Note: You only need to handle numbers 0-9
"""

def convert_numbers(string):
    pass


"""
Q2. 
Define a function named most_popular_word that:
1. declares a string parameter, 
2. determines which word occurred most frequently in the string, 
3. and returns the word and its frequency as a tuple. 
The time compelixty must be O(n).
Notes: This function should not be case sensitive
Assume the string contains only letters
"""
def most_popular_word(string):
    pass

"""
Q3.

The reserve ratio is the amount of each deposite that a bank must hold in
its reserves. The remainer of the money may be loaned out. That is, if the 
resever ratio is .2 then the bank may loan out (initial_value * .8). 
The person who receives the loan can the deposite it in their bank, which keeps 20% 
in the reserves and loans out the other 80% bring the total amount of money in the
economy to initial_value + (initial_value * .8) + ((initial_value * .8) * .8).


F(0) = initial value
F(N) = F(N) + (F(N-1) * 0.8)

Define a function named money_multiplier that:
1. declares parameters for the value of the account (float) and the number of
   loan given (int),
2. uses recursion to compute the total amount of money in the economy (float) after the 
   specified number of loans are given out,
3. and returns the computed value 

Assume the reserve ratio is locked at .2
"""

def money_multiplier(value, n):
    pass


"""
Q4.
Write a function that given a list of integers
will remove all duplicate integers from the list
and return the list without duplicates.
This function must be non_destructive.
Add exception handling code in your function above, to handle
unexpected values or types that may be passed in. The function 
should return None when it receives None as the input_list
parameter, and should throw an AttributeError exception in case of
other types.
"""
def remove_duplicates(input_list):
    pass

"""
Write a function that given a string that contains 
parenthesis, determines if they are balanced or not.
Assume that ( and ) are the only parethesis in the string.

Eg.
( -> False
) -> False
(()) -> True
()() -> False
"""
from node_stack import Stack
def is_balanced(string):
    pass

