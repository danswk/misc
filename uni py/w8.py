
#Functions to import - you may not import additional functions.
from random import shuffle
from time import perf_counter
import matplotlib.pyplot as plt

#Part A Sorting

#Question A1 Mergesort Data
def mergesort(mylist):
    if len(mylist)<=1:
        return mylist
    else:
        m=len(mylist)//2
        l=mergesort(mylist[:m])
        r=mergesort(mylist[m:])
        result=[]
        i=j=0
        while len(result)<len(r)+len(l):
            if l[i]<r[j]:
                result.append(l[i])
                i+=1
            else:
                result.append(r[j])
                j+=1
            if i==len(l) or j==len(r):
                result.extend(l[i:] or r[j:])
                break
        return result
listlengths=[]
sorttimelist=[]
for i in range(1,11):
      listlengths.append(2**i)
      mylist=list(range(2**i))
      shuffle(mylist)
      time_start=perf_counter()
      mergesort(mylist)
      time_end=perf_counter()
      sorttime=time_end-time_start
      sorttimelist.append(sorttime)
print(sorttimelist)
#The printed list is the data wherein the ith
#entry is the time tM(i) necessary for merge-
#sort to sort lists of randomly chosen elements
#of length 2^i for i=1,...,10.

#Question A2 Mergesort Plot
plt.figure('A')
plt.loglog(listlengths,sorttimelist,'o-')
plt.xlabel('Length of list (2^i intervals)')
plt.ylabel('Time taken to sort (s)')
#This plot illustrates that the mergesort function
#takes longer to sort lists of longer length, with
#expected positive correlation. This function
#splits the original list into lists l and r of
#(roughly) half the original length and recurs on
#them (logn) before merging the (now single) n
#elements (n*logn). Thus, the complexity of the
#function is O(nlogn). If we plot y=xlogx, we see
#it takes a similar form with strong positive
#correlation, supporting the stated complexity.

#Question A3 Insertionsort
def insertionsort(somelist):
    if len(somelist)<=1:
        return somelist
    else:
        sortedlist=somelist
        for i in range(len(somelist)):
            for j in range(i):
                if somelist[j]>somelist[i]:
                    sortedlist.insert(j,somelist.pop(i))
        return sortedlist

#Question A4 Insertionsort Plot
listlengths=[]
sorttimelist=[]
for i in range(1,11):
      listlengths.append(2**i)
      mylist=list(range(2**i))
      shuffle(mylist)
      time_start=perf_counter()
      insertionsort(mylist)
      time_end=perf_counter()
      sorttime=time_end-time_start
      sorttimelist.append(sorttime)
plt.figure('A')
plt.loglog(listlengths,sorttimelist,'o-')
#This plot over the existing plot for tM(i)
#illustrates that the insertionsort function is
#faster than the mergesort function at sorting
#lists of shorter length, but is overtaken when
#lists reach length of approximately 10^2
#(between 2^6 and 2^7). In the worst case, this 
#function compares the list's n elements (n-1
#comparisons) and shifts the entire sorted 
#subsection before inserting the next element
#(n-1 swaps). Thus, the complexity of the
#function is quadratic, O(n^2). If we plot y=x^2,
#we see it takes a similar form with more shallow
#gradient towards the origin which increases
#steadily, supporting the stated complexity.

#Question A5 Bubblesort Code
def bubblesort(mylist):
    n=len(mylist)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if mylist[j]>mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
    return mylist

#Question A6 Bubblesort Plot
listlengths=[]
sorttimelist=[]
for i in range(1,11):
      listlengths.append(2**i)
      mylist=list(range(2**i))
      shuffle(mylist)
      time_start=perf_counter()
      bubblesort(mylist)
      time_end=perf_counter()
      sorttime=time_end-time_start
      sorttimelist.append(sorttime)
plt.figure('A')
plt.loglog(listlengths,sorttimelist,'o-')
plt.title('tM(i) (blue), tI(i) (orange), tB(i) (green) against 2^i')
#This plot over the existing plots for tM(i) and
#tI(i) illustrates that the speed of the bubble-
#sort function comes between the other 2 for lists
#of shorter length, but is overtaken by the merge-
#sort function for lists of approximately 2^6 or 
#more elements. We see that bubblesort is the
#slowest of the 3 methods for large arrays,
#followed by insertionsort and then mergesort as
#the fastest. This is almost inverse to the result
#for small i, where mergesort is the slowest,
#outdone by the other 2 functions at similar rates.
#The bubblesort function's inner loop iterates
#n+(n-1)+...+1 times, meaning its complexity is
#O(n+(n-1)+...+1)=O(n(n+1)/2)=O(n^2). As before,
#the plot of y=x^2 is a similar parabolic shape,
#supporting the big O notation and plot of tB(i).

#Question A7
def bubblesortsorted(mylist):
    n=len(mylist)
    for i in range(n-1):
        swaps=0
        for j in range(0,n-i-1):
            if mylist[j]>mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
                swaps+=1
                if swaps==0:
                    break
    return mylist

#Question B8 triple_riffle
def triple_riffle(mylist):
    if len(mylist)%3==0:
        listlen=len(mylist)//3
        lista=mylist[:listlen]
        listb=mylist[listlen:2*listlen]
        listc=mylist[2*listlen:]
        new=[]
        for i in range(listlen):
            new.extend([listc[i],listb[i],lista[i]])
        return new
    else:
        return("Please enter a list with length divisible by 3.")
    
#Question B9 triple_riffle_repeat
def triple_riffle_repeat(mylist,n):
    rep=0
    while rep<n:
        mylist=triple_riffle(mylist)
        rep+=1
    return mylist
    
#Question B10 triple_riffle period
def period(m):
    if m%3==0:
        n=1
        while triple_riffle_repeat(list(range(m)),n)!=list(range(m)):
            n+=1
        return n
    else:
        return("Please enter an integer divisible by 3.")

#Question B11 triple_riffle analysis'''
#To check this function works, I will use m=21.
#Testing triple_riffle_repeat(list(range(21)),n)
#for 1<=n<=4 gives corresponding unsorted lists:
#[14, 7, 0, 15, 8, 1, 16, 9, 2, 17, 10, 3, 18, 11, 4, 19, 12, 5, 20, 13, 6]
#[4, 9, 14, 19, 2, 7, 12, 17, 0, 5, 10, 15, 20, 3, 8, 13, 18, 1, 6, 11, 16]
#[8, 17, 4, 13, 0, 9, 18, 5, 14, 1, 10, 19, 6, 15, 2, 11, 20, 7, 16, 3, 12]
#[2, 5, 8, 11, 14, 17, 20, 1, 4, 7, 10, 13, 16, 19, 0, 3, 6, 9, 12, 15, 18]
#n=5 gives the first sorted list (=list(range(21))):
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#Hence, we are expecting period(21)=5. This is
#true and so the function works for m=21.
#m=3:
#period(3)=2
#triple_riffle_repeat(list(range(3)),1)=[2,1,0] – unsorted
#triple_riffle_repeat(list(range(3)),2)=[1,2,0] – sorted as expected
#m=6:
#period(6)=6
#triple_riffle_repeat(list(range(6)),1)=[4,2,0,5,3,1] – unsorted
#triple_riffle_repeat(list(range(6)),2)=[3,0,4,1,5,2] – unsorted
#triple_riffle_repeat(list(range(6)),3)=[5,4,3,2,1,0] – unsorted
#triple_riffle_repeat(list(range(6)),4)=[1,3,5,0,2,4] – unsorted
#triple_riffle_repeat(list(range(6)),5)=[2,5,1,4,0,3] – unsorted
#triple_riffle_repeat(list(range(6)),6)=[0,1,2,3,4,5] – sorted as expected
#Evidently, the function works as intended.