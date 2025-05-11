def ValidMountainArray(A:list[int])->bool:
    if(len(A)<=3):
        return False
    i = 1
    while(i<len(A) and A[i-1]):
        i+=1
    
    if (i==1 or i==len(A)):
        return False
    
    while (i<len(A) and A[i]<A[i-1]):
        i+=1
    return i == len(A)
    
test = [0,3,2,1]
print(ValidMountainArray(test))
