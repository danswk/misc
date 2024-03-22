
# Ex 3 Template
# No need to import any libraries or modules this week!
# Please make sure your file runs, and submit only one .py file.
# Don't change the given function names!

# 3Ai
def greatestgcd(a,b,c):
    def gcd(x,y):
        while y>0:
            x,y=y,x%y
        return x
    return(max(gcd(a,b),gcd(b,c),gcd(a,b)))

# 3Aii
def evenodd(n):
    if n%2==0:
        return True
    else:
        return False
    
# 3Aiii
def listelements(m):
    if len(m)<4:
        return False
    else:
        return(m[0],m[1],m[-2],m[-1])
    
# 3Aiv
def double(m):
    for i in range(len(m)):
        m[i]*=2
    return(m)

# 3Av
def isprime(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**(1/2)+1)):
            if n%i==0:
                return False
        return True

# 3Bi
def dectobin(n):
    binary=[]
    while n>0:
        binary.append(n%2)
        n//=2
    binary.reverse()
    return binary

# 3Bii
def bintodec(binary):
    n=0
    binary.reverse()
    for i in range(len(binary)):
        n+=(2**i)*binary[i]
    return n

# 3C
def primesbetween(n,m):
    primes=list(range(n,m+1))
    for i in primes:
        j=2
        while i*j<=primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j+=1
    return(len(primes))
    #just returns all integers n to m inclusive?

# 3D
def sundaram(n):
    primes=list(range(1,n+1))
    for i in primes:
        j
    #?