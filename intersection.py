def intersection(numbers1,numbers2):
    result=[]
    seen=set(numbers1)
    for i in numbers2:
        if i in seen:
            result.append(i)
        if result==[]:
            return "no intersecion"


        
    
    return result
            
        
        
        

    
print(intersection([1,2,3,4,6],[2,4,6,8,7]))
print(intersection([11,22,33,44,66],[2,4,6,8,7]))
