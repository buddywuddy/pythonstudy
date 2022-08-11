"""
HANS PETTER LANGTANGEN
A Primer on Scientific Programming with Python
"""
##Chapter 1.1: Computing with formulas

"""
The first formula to consider concerns the vertical motion of a ball thrown in the air. 
From Newton's second law of motion, one can set up the mathematical model for the motion of the ball to y(t) = v0t - (1/2)gt^2
The first program can be written using python's built in math library to use it as a calculator:
"""


##SYNTAX:
# addition: x + n
# subtraction: x- n
# multiplication: x * n 
# division: x /n
# exponential: x ** n

"""EXAMPLE 1"""
print (5*0.6 - 0.5*9.81*0.6**2)

##The program can be optimized and esier to read/ follow by using variables
##Using the variable given by the orginal formula, the program can be written as follows:


"""EXAMPLE 2"""
v0 = 5
g = 9.81
t = 0.6
y = v0*t - 0.5*g*t**2
print (y)

##Naming variables can be very important as well, so alternate variables making the program easier to follow for those who did not write it is given by:

"""EXAMPLE 3"""
initial_velocity = 5
acceleration_of_gravity = 9.81
TIME = 0.6
VerticalPositionOfBall = initial_velocity*TIME - 0.5*acceleration_of_gravity*TIME**2

print (VerticalPositionOfBall)

##Alternatively, the variable names can be given in comments to keep the simplified variable names of the original equation:

"""EXAMPLE 4"""
#program for computing the height of a ball in vertical position
v0 = 5                      #initial velocity
g = 9.81                    #acceleration of gravity
t = 0.6                     #time
y = v0*t - 0.5*g*t**2       #vertical postion
print (y)

"""
Note that non english characters are not allowed and will jam up the code
"""

##Printf SYNTAX:
# Printf formatting allows programmers to output changeable type that can change to match the variables.

"""EXAMPLE 5"""
v0 = 5
g = 9.81
t = 0.6
y = v0*t - 0.5*g*t**2
print ('At t=%g seconds, the height of the ball is %.2f meters in the air. \n' % (t, y))

"""
\n can be used to  insert a line between text in a string
"""

##Printf EXTENSIONS:
# %s      a string
# %d      an integer
# %0xd    an integer paddled with x leaidng zeros
# %f      decimal notation with 6 decimals
# %e      compact scientific notation, e in the exponent
# %E      compact scientific notation, e in the exponent
# %g      compact decimal or scientific notation (with e)
# %G      compact decimal or scientific notation (with E)
# %xz     format z right-adjusted in a field of width x
# %-xz    format z left-adjusted in field of width x
# %.yz    format z with y decimals
# %x.yz   format z with y decimals in a field of width 
# %%      the percentage sign % itself

"""EXAMPLE 6"""
v0 = 5
g = 9.81
t = 0.6
y = v0*t - 0.5*g*t**2
print ("""At t=%f s, 
a ball with initial velocity v0=%.3E m/s 
is located at the height %.2f m."""
% (t, v0, y))

"""
Note that triple-quoted strings can be used for text that spans across multiple lines^^
"""
##Format String SYNTAX:
# format string syntax allows a programmer to use slots to insert variables that are recognized by {curly brackets} rather than a percentage sign.
# the variables and their values must be listed at the end as shown:

"""EXAMPLE 7"""
print ("""
At t={t:f} s, a ball with
initial velocity v0={v0:.3E} m/s
is located at the height {y:.2f} m.
""" .format (t=t, v0=v0, y=y))

##END CHAPTER 1.1