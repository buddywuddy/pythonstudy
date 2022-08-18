"""
HANS PETTER LANGTANGEN
A Primer on Scientific Programming with Python
"""
##Chapter 1.3: Another Formula: Celcius-Farenheit Conversion

"""
The next formula example involves the formula for converting temperature measured in Celcius to the corresponding Farenheit measurement.
the formula can be written as F = (9/5)C + 32, (1.3) where C represents degrees Celcius and F represents degrees Farenheit
The goal now is to write a computer program that can compute F from (1,3) when C is givejn.
"""

#A straightforward coding of the formula is written as follows:
"""EXAMPLE 1"""
C = 21
F = (9/5)*C + 32
print(F)

"""
Note that the parenthesis around (9/5) are not strictly need3ed, but remove and doubt that 9/5*C could mean 9/(5*C)
"""
##Verifying the results
# The results in this case should be easy to verify because the formula can be plugged into a calculator, but the program outputs 69.8 while the calculator gives 53.
# the reason for this indescrepency is because of float and integer division.

##Float and Integer division:
# The error in the program is one of the most common errors in mathematical software.
# In many computer languages, there are two types of division: (float and integer division)
# Float division occurs when 9.5 becomes 1.8 in decimal notation
# Integer division a/b with integers a and b result in an integer that is truncated (mathematically rounded down).
    # More precisely, the result is the ;argest integer c such that bc<=a, which implies that 9/5 becomes 1 since 1*5<9 while 2*5=10>9
# Many computer languages including C, C++, Python, and Java interpret a division operation as integer division if both a and b are integers.
# Thus in the previous program, (9/5) was interpreted as 1 because of the rules of integer division, skewing the results by a significant amount.

##Objects in python:
