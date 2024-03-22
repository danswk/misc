#MATH2920 Miniproject Sparse Rulers Template File

#import files here
from itertools import combinations
from statistics import mean
import matplotlib.pyplot as plt

#Part 1
#Q1(a)
def reach(myruler):
    for i in range(len(myruler)-1):
        if myruler[i]<0:
            return('Please input a ruler with positive distances.')
        elif myruler[i]>myruler[i+1]:
            return('Please input a ruler with distances in increasing order.')
        elif max(myruler)<1:
            return('Please input a ruler of minimum length 1.')
        for j in range(len(myruler)):
            if myruler[j]-int(myruler[j])!=0:
                return('Please input a ruler with integer distances.')
    return myruler[-1]
        
def order(myruler):
    for i in range(len(myruler)-1):
        if myruler[i]<0:
            return('Please input a ruler with positive distances.')
        elif myruler[i]>myruler[i+1]:
            return('Please input a ruler with distances in increasing order.')
        elif max(myruler)<1:
            return('Please input a ruler of minimum length 1.')
        for j in range(len(myruler)):
            if myruler[j]-int(myruler[j])!=0:
                return('Please input a ruler with integer distances.')
    return len(myruler)

#Q1(b)
def isitaruler(mylist):
    for i in range(len(mylist)):
        if mylist[i]-int(mylist[i])!=0:
            return False
    if mylist[0]!=0:
        return False
    for j in range(len(mylist)-1):
        if mylist[j]>mylist[j+1]:
            return False
    return True

#Q1(c)
def sparsenkrulers(n,k):
    if n+1>=k>=2:
        listofrulers=[]
        for x in combinations(list(range(1,n)),k-2):
            thislist=[0]
            for i in x:
                thislist.append(i)
            thislist.append(n)
            listofrulers.append(thislist)
    else:
        return('Please enter n, k such that n+1 >= k >= 2.')
    return listofrulers

#Q1(d)
def ismyrulercomplete(myruler):
    diffs=[abs(a-b) for a,b in combinations(myruler,2)]
    k=1
    while k<=max(myruler):
        isincl=diffs.count(k)
        if isincl==0:
            return False
        k+=1
    return True

#Part 2
#Q2(a)
def ismyrulergolomb(myruler):
    diffs=[abs(a-b) for a,b in combinations(myruler,2)]
    reps=[]
    for k in range(max(diffs)+1):
        rep=diffs.count(k)
        reps.append(rep)
    for l in reps:
        if l>1:
            return False
    return True

#Q2(b)
def listofgolombrulers(n):
    rulers=[]
    k=3
    while k<=n:
        golomb=sparsenkrulers(n,k)
        for i in golomb:
            isgolomb=ismyrulergolomb(i)
            if isgolomb == True:
                rulers.append(i)
        k+=1
    return rulers

def listofcompleterulers(n):    
    rulers=[]
    k=3
    while k<=n:
        complete=sparsenkrulers(n,k)
        for i in complete:
            iscomplete=ismyrulercomplete(i)
            if iscomplete == True:
                rulers.append(i)
        k+=1
    rulers.append(list(range(n+1)))
    return rulers
#Comment:
#Running the function for n=0, n=1 and n=2 simply returns the list up to and
#including n as expected, since no other complete rulers of such low order
#exist. For example, [0,2] is not complete because there is no way to measure
#distance 1. n=3 produces the first result with minimal rulers that omit some
#marks from 0 to n. n=4 gives 4 lists, n=5 gives 9, n=6 gives 17 and so on.
#We see that the number of complete rulers increases at a greater rate as n
#increases. This makes sense as for larger n, there are more list elements
#available to draw differences from.

# #Q2(c)
def ErdosTuran(m):
    k=0
    ruler=[]
    if m>2:
        while k<m:
            point=2*m*k+(k**2%m)
            ruler.append(point)
            k+=1
    return ruler
#Comment:
#Running this function for different values of n–
#n=3:
#[0,7,13]
#n=4:
#[0,9,16,25]
#n=5:
#[0,11,24,34,41]
#n=6:
#[0,13,28,39,52,61]
#n=7:
#[0,15,32,44,58,74,85]
#n=8:
#[0,17,36,49,64,81,100,113]
#We can observe from these results that the first element is always 0. The
#second element in the list increases by 2 with each iteration. The third
#by 3, 8, 4, 4 and 4 respectively, the fourth by 9, 5, 5 and 5 respectively,
#and the fifth by 9, 6 and 6 respectively. It seems as though for each list
#index, the differences between the values at that index 'round off' to the
#index number +1 as n increases. Using the ismyrulercomplete and
#ismyrulergolomb functions for the ruler output for n=8, we see that neither
#are true. This is as expected, as the reach is too high for a ruler of such
#order to cover using only the differences between its markings.

#Part 3
#Comparing the order of complete sparse rulers and Golomb rulers of reach n–
def lengthofrulers(n):
    completelens=[]
    golomblens=[]
    for i in list(listofcompleterulers(n)):
        leni=len(i)
        completelens.append(leni)
    for j in list(listofgolombrulers(n)):
        lenj=len(j)
        golomblens.append(lenj)
    print('Mean length of complete ruler of reach',n,'is',mean(completelens))
    print('Mean length of golomb ruler of reach',n,'is',mean(golomblens))
#Running this function for different values of k–
#k=3:
#Mean complete length is 3
#Mean golomb length is 3
#k=6:
#Mean complete length is 5.1875
#Mean golomb length is 3.3333333333333335   
#k=9:
#Mean complete length is 6.960629921259843
#Mean golomb length is 3.6923076923076925
#k=12:
#Mean complete length is 8.604863221884498
#Mean golomb length is 4.068965517241379
#k=15:
#Mean complete length is 10.166751527494908
#Mean golomb length is 4.382716049382716
#Through this data, we see that on average, complete rulers are longer (have
#greater order) than golomb counterparts of the same reach. We also see that
#the mean length of complete rulers increases at a more rapid rate than
#golomb rulers. This is as expected, since the latter has an additional
#requirement that all differences between marks are distinct.
#Plotting this data up to k=15 (complete)–
    plotcompletelens=[]
    for i in range(3,n):
        for j in list(listofcompleterulers(i)):
            lenj=len(j)
            plotcompletelens.append(lenj)
        plt.figure('A')
        plt.plot(i,mean(plotcompletelens),'o-',color='r')
        plt.xlabel('n')
        plt.ylabel('Mean order of rulers')
#Observing the graph, we see that although the reach takes integer values and
#the mean order decimals, they actually form a perfect positive correlation.
#Plotting this data up to k=15 (golomb)–
    plotgolomblens=[]
    for i in range(3,n):
        for j in list(listofgolombrulers(i)):
            lenj=len(j)
            plotgolomblens.append(lenj)
        plt.figure('A')
        plt.plot(i,mean(plotgolomblens),'o-',color='g')
        plt.title('Mean orders of complete (red) and golomb (green) rulers of reach n')
#Observing the graph, we see that as above, the mean order of golomb rulers
#increases with the reach but at a much slower rate, barely exceeding 4 at
#n=15.
#Finding the percentage of complete rulers that are also golomb–
def percomplete(n):
    # rulers=[]
    per=[]
    rulers=list(listofgolombrulers(n))
    for i in rulers:
        iscomplete=ismyrulercomplete(i)
        if iscomplete == True:
            per.append(i)
    print('Percentage of golomb rulers of order',n,'that are complete is',(len(per)/len(rulers))*100)
#Running the function for different values of n, we can observe that there
#are no perfect golomb rulers (complete, measuring all distances) of order
#higher than 3:
#percomplete(3)=100.0
#percomplete(4)=0.0
#This makes sense if we observe the rulers directly:
#listofgolombrulers(3)=[[0,1,3],[0,2,3]]
#In the first ruler, 0–1 measures 1, 1–2 measures 2 and 0–3 measures 3.
#In the first ruler, 2–3 measures 1, 0–2 measures 2 and 0–3 measures 3.
#Thus, both rulers are complete (perfect golomb).
#listofgolombrulers(4)=[[0,1,4],[0,3,4]]
#In the first ruler, 0–1 measures 1 but no pair of elements measures 2.
#In the first ruler, 3–4 measures 1 but no pair of elements measures 2.
#Thus, neither rulers are complete.
#Plotting this data up to m=10–
def plotper(m):
    plotper=[]
    rulers=list(listofgolombrulers(m))
    for j in range(3,m+1):
        for k in rulers:
            iscomplete2=ismyrulercomplete(k)
            if iscomplete2 == True:
                plotper.append(k)
            eachper=(len(plotper)/len(rulers))*100
        return eachper
r=range(11)
l=list(plotper(l) for l in r)
plt.figure('B')
plt.plot(r,l,'o-',color='b')
plt.xlabel('n')
plt.ylabel('Percentage of golomb rulers that are complete')
#Observing the graph, we see that all golomb rulers of order 3 are
#complete, and that 1/3 of golomb rulers of order 6 are complete, but
#all rulers of other orders are imperfect (unable to measure all
#distances).