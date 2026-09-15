def reverse_in_place(numbers):
    
    
    left=0
    right=len(numbers)-1
    while(left<right):
        numbers[left],numbers[right]=numbers[right],numbers[left]
        left+=1
        right-=1
    return numbers

print(reverse_in_place([8,9,10,12]))