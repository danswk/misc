# Template file for Week 2
# Lines that start with '#'
# are comments and are ignored
# by Python.

#2A Write your functions below
# Example, a function which takes an integer and squares it:
def squared(x):
    xx=x**2
    return xx

## DO NOT CHANGE THE FUNCTION NAMES!! ##
# (i)  
def cubed(x):
    xxx=x**3
    return xxx

# (ii) 
def meanpair(x,y):
    z=(x+y)/2
    return z

# (iii) 
def pyth(a,b,c):
    if a<=b<=c:
        if a**2+b**2==c**2:
            return True
        elif a**2+b**2!=c**2:
            return False
    else:
        print("Please enter three integers in increasing order.")
    
# (iv) 
def meanlist(x):
    return sum(x)/len(x)

# (v) 
import math
def mygcd(x,y):
    if x>0 and y>0:
        return math.gcd(x,y)
    else:
        print("Please enter two positive integers.")

# (vi)
def meanpair_or_gcd(x,y):
    if meanpair(x,y)>2*mygcd(x,y):
        return meanpair(x,y)
    else:
        return 2*mygcd(x,y)

#2B Insert your Euclidean algorithm program lines here:
def Euclid(a,b):
    if a!=0 and b!=0:
        while b>0:
            t=b
            b,a=a%b,t
        return a
    else:
        print("Please enter two non-zero integers.")

#2C Insert your extended Euclidean algorithm here:
def ExtEuclid(a,b):
    x=0
    xprev=1
    y=1
    yprev=0
    if a>b>0:
        while b>0:
            q=a//b
            a,b=b,a%b
            x,xprev=xprev-q*x,x
            y,yprev=yprev-q*y,y
            d=a*x+b*y
        return(d,x,y)
    else:
        print("Please enter two positive integers in decreasing order.")
    #d does not give gcd(a,b)?

#2D Insert your counting-steps Euclid program here:
def CountEuclid(a,b):
    s=0
    if a>b>0:
        while b>0:
            t=b
            b,a=a%b,t
            s+=1
        return (a,s)
    else:
        print("Please enter two positive integers in decreasing order.")
        
        
        def primesbetween(n,m):
            primes=list(range(n,m+1))
            for i in primes:
                j=2
                while i*j<=primes[-1]:
                    if i*j in primes:
                        primes.remove(i*j)
                    j+=1
            return(primes)   
        
        while b>0:
            a,b=b,a%b
            break
        gcdab=a
        while c>0:
            b,c=c,b%c
            break
        gcdbc=b
        while a>0:
            c,a=a,c%a
            break
        gcdac=c


for i in range(10)