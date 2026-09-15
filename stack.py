def reverse_string(text):
    stack=[]
    for i in text:
        c=stack.append(i)
    result=""
    while stack:
         result+=stack.pop()
    return result

print(reverse_string("achook"))