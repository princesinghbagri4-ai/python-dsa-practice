def is_balanced(text):
    stack=[]
    for ib in text:
        if(ib=="("):
            stack.append(ib)
        elif(ib==")"):
            if not stack:
        
              return False
        
            stack.pop()
    return stack==[]
        

            

print(is_balanced("(())("))
print(is_balanced("(())()"))


