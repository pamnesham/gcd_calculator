#!python 3

#Function to find the greatest common denominator
def gcd(a, b):
    if a == 0:      #make sure a is the larger number
        return b
    if b == 0:
        return a
    if a < 0:       #make negative numbers positive
        a = a * -1
    if b < 0:
        b = b * -1
    if b > a:
        greater = b
        lesser = a
    else:
        greater = a
        lesser = b
        
    while lesser > 0:       #calculate gcd
        q = greater//lesser
        r = greater-(lesser*q)
        greater = lesser
        lesser = r
    return(greater)
