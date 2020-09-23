def glovepairs(array,n):
    count=0
    array.sort()
    i=0
    while i<(n-1):
        if(array[i]==array[i+1]):
            count +=1
            i=i+2
        else:
            i +=1
    return count
n=int(input("Enter the number of gloves:"))
array=list(map(int,input("Enter the elements comprising the interger values corresponding to sock colour:").split(' ')[:n]))
print("The total number of matching pairs of gloves that jack can sell:",glovepairs(array,n))
