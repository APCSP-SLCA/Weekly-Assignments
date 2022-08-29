
# Name:
# Group Members:
# Date:

# Remember to also comment each function with the following:
#       * description of each functions's purpose
#       * description of each functions's function
#       * pseudocode and/or flow diagram (create a new file for flow diagrams)


import math # we need to import the math module to use square root and power functions


def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

###############################################################################

def isFactor(n, f):
    # return True if f is a factor of n
    # return False otherwise

    return -1

def isMultiple(n, m):
    # return True if m is a multiple of n
    # return False otherwise

    return -1

# use math.sqrt(x) to find the square root of x
# use math.pow(x, 2) or x**2 to find x^2

def distance(x1, y1, x2, y2):
    # return the distance between the points (x1, y1) and (x2, y2)
    # Hint: Remember the Distance Formula?

    return -1

def fabricYards(inches):
    # returns the smallest number of whole yards of fabric

    return -1
 
def fabricExcess(inches):
    # returns the number of inches of excess fabric that must be purchased (as purchases must be in whole yards)
    # Hint: You may use fabricYards(inches), which you just wrote!

    return  -1

###############################################################################

def testIsFactor():

    # no where close to an exhaustive test
    # highly recommend for you to add your
    # own tests
    
    assert isFactor(6, -1)
    assert not isFactor(6, 0)
    assert isFactor(6, 1)
    assert isFactor(6, 2)
    assert isFactor(6, 3)
    assert not isFactor(6, 4)
    assert not isFactor(6, 5)
    assert not isFactor(6, 6)

    return

def testIsMultiple():

    # no where close to an exhaustive test
    # highly recommend for you to add your
    # own tests

    assert isMultiple(3, -3) == True
    assert isMultiple(3, 1) == False
    assert isMultiple(3, 3) == True
    assert isMultiple(3, 4) == False
    assert isMultiple(3, 5) == False
    assert isMultiple(3, 6) == True

    return

def testDistance():

    # no where close to an exhaustive test
    # highly recommend for you to add your
    # own tests

    assert distance(0, 0, 0, 10) == 10
    assert distance(0, 0, 1, 1) == math.sqrt(2)
    assert distance(0, 0, -10, -10) == 10*math.sqrt(2)
    assert distance(0, 1, 2, 3) == math.sqrt(8)

    return

def testFabricYards():

    # no where close to an exhaustive test
    # highly recommend for you to add your
    # own tests

    assert fabricYards(35) == 1
    assert fabricYards(36) == 1
    assert fabricYards(37) == 2
    assert fabricYards(72) == 2
    assert fabricYards(73) == 3
    assert fabricYards(74) == 3
    assert fabricYards(75) == 3

    return

def testFabricExcess():

    # no where close to an exhaustive test
    # highly recommend for you to add your
    # own tests

    assert fabricExcess(35) == 1
    assert fabricExcess(36) == 0
    assert fabricExcess(37) == 35
    assert fabricExcess(72) == 0
    assert fabricExcess(73) == 35
    assert fabricExcess(74) == 34
    assert fabricExcess(75) == 33

    return

def testAll():
    # feel free to comment out any subtests as you develop
    # your program, but be sure to uncomment all the tests
    # when you submit!

    testIsFactor()
    testIsMultiple()
    testDistance()
    testFabricYards()
    testFabricExcess()

    return

def main():

    testAll()
    return


# this code block only runs if the file is *not* imported
if __name__ == "__main__":
    main()