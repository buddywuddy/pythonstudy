"""
HANS PETTER LANGTANGEN
A Primer on Scientific Programming with Python
"""
##Chapter 1.2: Computer Science Glossary

"""
Programmers often use very specific vocabulary when talking about programming.
Some words that are common in the English language have a much different menaing in coding language such as "library" or "statement"
This chapter is dedicated to becoming familiar with Pregramming lingo, and what someone refers to when they say "source code" r "code snippet"
"""


##VOCABULARY
# program/ code:        a sequence or set of instructions in a programming language for a computer to execute
# segment:              a collection of consecutive statements from a program
# code snippet:         a small amount of code design to illustrate a specific purpose
# application:          a word often used in exchange for program and code
# source code:          the same text that constitutes the program
#                       source code can be found in one or more text files (.txt) or program files (.py, .js, etc.) whose extensions realte to the given language
# running a program:    executing the program or file, compiling the code
# executable:           the file being executed
# library:              a collection of generally useful program pieces that can be applies in many different contexts
#                       having libraries allows for a programmer to skip through coding specific functions that others have already prigrammed
# modules/packages:     define the sections of functionality (math module, graphing module, etc.)
# algorithm:            a list set of instructions used to solve problems or perform tasks based on the understanding of availible alternatives
# implementation:       the probcess of writing and testing a program, also known as verification
# bug:                  an error in the program
# debugging:            the process of locating and removing bugs
# statements:           there are many kinds of statements, for example:
    # assignment statement: a statement that assigns a value to a variable (ex. v0 = 3)
    #                       an assignment statement such as (y = y + 3) does not make mathematical sense but in programming, 
    #                       this statement simply means that the previous value of y is now equal to 3 greater than it was. 
    #                       in this instace, the left-hand side of the assignment contains the expression, while the right-hand side is assigned.
    # print statement       a statement that displays the outcome of a given sequence (ex. print (y))

"""EXAMPLE 1"""
vO = 3
#this is an example of an assignment statement as decribes above.

"""EXAMPLE 2"""
print (y)
#this is an example of a print statement as describes above.

"""EXAMPLE 3"""
v0 = 3; g = 9.81; t = 0.6
y = v0*t - 0.5*g*t**2
print (y)
#it is common to have many assignment statements in one line that are separated each by a semi-colon, like its use for separate clauses in english

"""EXAMPLE 4"""
y = 3
print (y)
y = y + 4
print (y)       
y = y*y         # the syntax y**2 is an equivalent of y*y
print (y)

##VOCABULARY (cont.)
# syntax:               the specific rules and format that a computer program must follow to be correctly executed in a specific language

"""EXAMPLE 5"""
myvar = 5.2
print (Myvar)

"""
This would result in a syntax error because the variable "myvar" does not match when called by the print statement deu to the capitalized "M"
This means that "myvar" is an uncalled variable, while "Myvar" was never defined
"""

##VOCABULARY (cont.)
# blank/whitespace:     spaces in a computer program. blanks are not essential for python in most cases, but do help user readability.

"""EXAMPLE 6"""
v0=3;g=9.81;t=0.6;y=v0*t-0.5*g*t**2;print(y)
#adding blanks in this case becomes necessary in order to find errors in the code which is the difficult part of programming

##VOCABULARY (cont.)
# input data:           information that must be known beforehand
# output data:          the result of running a program
# user:                 a human interacting with a program
# operating system:     a collection of program that manages the hardware and software resources (ex. Windows, MacOS, Linux, etc.)

##END CHAPTER 1.2