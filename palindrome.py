def is_palindrome(numbers):
    left=0
    right=len(numbers)-1

    while(left<right):
        if(numbers[left]==numbers[right]):
            
            left+=1
            right-=1
        else:
            return False
    return True 
    



print(is_palindrome("mass"))
print(is_palindrome("madam"))