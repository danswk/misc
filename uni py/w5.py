#Exercise 5A solutions 

#import modules here
import numpy as np
import matplotlib.pyplot as plt

#Exercise 5A(i)
def collatzseq(n):
    col=[]
    col.append(n)
    while n>1:
        if n%2==0:
            n/=2
            col.append(n)
        else:
            n=3*n+1
            col.append(n)
    col=[round(x) for x in col]
    return col

#Exercise 5A(ii)
def collatzcount(n):
    s=0
    while n>1:
        if n%2==0:
            n/=2
            s+=1
        else:
            n=3*n+1
            s+=1
    return s

#Exercise 5A(iii)

#Write your code that plots your graph here (not commented out)
n=np.arange(1,1001,1)
sn=[collatzcount(ni) for ni in n]
plt.figure('A')
plt.plot(n,sn,'o-')
plt.title('Steps in Collatz sequence')
plt.xlabel('n')
plt.ylabel('S(n)')
    
#Exercise 5A(iv)

#Write your answer as a comment here (including including any code you used to obtain it but commented out.)
# n=np.arange(1,1001,1)
# bln=[]
# for ni in n:
#     sn=[collatzcount(ni)]
#     for sni in sn:
#         if sni<ni/10:
#             bln.append(True)
#         else:
#             bln.append(False)
# print((bln.count(True)/1000)*100)
    #44.3%

#Exercise 5A(v)

#Write your code that plots your graph(s) here (not commented out)
n=np.arange(1,1001,1)
mn=list((max(collatzseq(ni)) for ni in n))
plt.figure('B')
plt.plot(n,mn,'o-')
plt.title('Maximum in Collatz sequence')
plt.xlabel('n')
plt.ylabel('max(n)')
    
#Reminder: check your programme runs before submission!
#Your code should generate any figures when run. Do not upload/submit figures separately.