#MATH2920 Week 4 Exercise Template

'''
The following line contains all the 
functions you need to import
for this exercise sheet - please don't import
any more!
'''
from math import atan,pi,cos,sin,sqrt

# 4A Write your functions below
# E.g., a function which takes an integer and squares it
# def squared 

def squared(x):
    xx=x**2
    return xx

## DO NOT CHANGE THE FUNCTION NAMES!! ##
#(1)
def mypoly(x):
    return(x**3-x**2)

#(2)
def sumproduct(x,y):
    return(x+y,x*y)

#(3)
def three_means(x):
    am=sum(x)/len(x)
    pro=1
    for i in x:
        pro*=i
        gm=pro**(1/len(x))
    den=0
    for i in x:
        den+=1/i
        hm=len(x)/den
    return(am,gm,hm)

#(4)
def narayana(n):
    cow=[]
    i=1
    while i<=n:
        while i<=3:
            cow.append(1)
            i+=1
        cow.append(cow[-1]+cow[-3])
        i+=1
    return cow

#(5)
def polar_to_cartesian(rho,phi):
    x=rho*cos(phi)
    y=rho*sin(phi)
    return(x,y)

#(6)
def cartesian_to_polar(x,y):
    if x==y==0:
        return(0,0)
    rho=sqrt(x**2+y**2)
    phi=atan(y/x)
    if x<=0 and y>=0 or x<=0 and y<=0:
        phi+=pi
    elif x>=0 and y<=0:
        phi+=2*pi
    return(rho,phi)

## DO NOT CHANGE THE FUNCTION NAMES!!
#4B
#(1)
def horner(x,coeffs):
    coeffs.reverse()
    px=0
    for i in coeffs:
        px=x*px+i
    return px

#(2)
#(a)
print(horner(2,[1,5,1,1]))
    #23
#(b)
print(horner(sqrt(3),[5,0,-1]))
    #2.0000000000000004

# Are the answers exact? (Answer as comment):
#The solution to (a) is exact as it is integer
#(whose value can be verified as the solution to
#P(x)=x^3+x^2+5x+1 at x=2.)
#The solution to (b) is not exact as sqrt(3) is
#a floating point number represented in Python
#by base 2 binary fractions. Since most decimal
#fractions cannot be represented as their exact
#value due to limitation in unique combinations
#of the underlying set finite base 2 fractions,
#there is slight discrepancy between the solution
#generated by Python and the true solution. We
#can see this in computing (sqrt(3))**2, which
#does not return 3 but rather 2.9999999999999996.

#(3)
# type print command here:
print(horner(1/2,[1,-1/2,1/3,-1/4,1/5]))
    #0.8145833333333333

#(4)     
# a - type print command here:
#(x-2)^4=x^4-8x^3+24x^2-32x+16
print(horner(2.0001,[16,-32,24,-8,1]))
    #-3.552713678800501e-15

# b and c - comment here:
#This solution differs from the true solution,
#((2.0001-2)^4=(0.0001)^4=)1e-16, by a margin
#of 3.452713678800501e-15. Since the difference
#is extremely small, the value given is rather
#accurate, but not exactly correct, again due to
#the handling of floating point numbers.
#Evaluating the polynomial (x-2)^4 at x=2.0001
#using the Horner's method function shows that
#this value of x gives a narrow approximation 
#for the single root at x=2 through the proximity
#of its function value to 0.

#(5)
def horner_ternary_to_dec(x):
    dec=0
    for i in x:
        dec=3*dec+i
    return dec