def missingnumber(numbers):
    sum=0
    
    for i in numbers:
        sum+=i
    n=len(numbers)+1
    sum1=(n*(n+1))/2
    mnum=sum1-sum
    return mnum

    
print(missingnumber([1,2,3,4,5,6,7,9]))

    