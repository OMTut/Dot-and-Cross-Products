#!/usr/bin/env python3

#import math library and symbolic
import math
from sympy import *
#from sympy import sympify
x, y, z, t = symbols('x y z t ')
k, m, n = symbols('k m n', integer = True)
f, g, h = symbols('f g h', cls=Function)

# Take user input to build 2 vectors
# Ask if user wants to do a Dot Product or Cross Product
# Execute
# Ask if the user wants to do another

#Take User Input and build vectors 1 and 2
def first_vector():
    i = 0
    while len(v1) < 3:
        if i == 0:
            val = 'x'
        elif i == 1:
            val = 'y'
        else:
            val = 'z'
        number = input("Enter the " + val + "-value for vector 1: ")
        v1.append(number)
        i += 1
    print("Vector 1 is complete: " + str(v1) + '\n')

def second_vector():
    i = 0
    while len(v2) < 3:
        if i == 0:
            val = 'x'
        elif i == 1:
            val = 'y'
        else:
            val = 'z'
        number = input("Enter the " + val + "-value for vector 2: ")
        v2.append(number)
        i += 1
    print("Vector 2 is complete: " + str(v2) + '\n')

# Ask if the user wants another
def repeat_prob():
    repeatChoice = input("Do another: ")
    while True:
        if repeatChoice == 'y':
            break
        if repeatChoice == 'n':
            print("The End")
            break
        repeatChoice = input("Please Enter y or n: ")
    return repeatChoice

def probType():
    probChoice = input("Enter 1 for Dot Product or 2 for Cross Product: ")
    while True:
        if probChoice == '1':
            break
        if probChoice == '2':
            break
        probChoice = input("Please enter 1 for Dot Product or 2 for Cross Product: ")
    return probChoice

#Main Code
repeat = 'y'
while repeat == 'y':
    # Vector Arrays - empty arrays
    v1 = []
    v2 = []

    print("Welcome to the Dot and Cross Product Script.")
    print("Let's build vector 1.")
    print("Please be aware of syntax. Exponents are epxressed with ** instead of ^. Example: 3sin(x)^2 would be 3*sin(x)**2")
    first_vector()

    print("Awesome. Now let's build vector 2.")
    print("Please be aware of syntax. Exponents are epxressed with ** instead of ^. Example: 3sin(x)^2 would be 3*sin(x)**2")
    second_vector()

    #Easily used variables built from the Vector lists
    v1x = sympify(v1[0])
    v1y = sympify(v1[1])
    v1z = sympify(v1[2])
    v2x = sympify(v2[0])
    v2y = sympify(v2[1])
    v2z = sympify(v2[2])

    probChoice = probType() 
    if probChoice == '1':

        #Dot Product logic
        dot_prod  = ((v1x*v2x)+(v1y*v2y)+(v1z*v2z))
        print('Dot Product: ' + str(dot_prod) + '\n')
    elif probChoice == '2':

        #Cross Product logic
        # I repeat the Dot Prod code here only to make it easier to see the grouping in Choice 2. Since the Dot Product is used in both Choice 1 & 2, you could run dot_prod only once before the if statements
        dot_prod  = ((v1x*v2x)+(v1y*v2y)+(v1z*v2z))
        cross_prod = [(v1y*v2z)-(v1z*v2y), (v1z*v2x)-(v1x*v2z), (v1x*v2y)-(v1y*v2x)]
        
        #Magnitude & Theta Logic
        magv1 = sqrt((v1x**2)+(v1y**2)+(v1z**2))
        magv2 = sqrt((v2x**2)+(v2y**2)+(v2z**2))
        theta = (dot_prod/(magv1*magv2))
        
        #Print Statements
        print('Magnitude of vector 1: ' + str(magv1))
        print('Magnitude of vector 2: ' + str(magv2))
        print('The angle between vector 1 and 2: '+str(theta))
        print('Cross Product: ' + str(cross_prod) + '\n')
    
    repeat = repeat_prob()