def count_frequency(text):
    frequency={}
    
    for i in text:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    return frequency
print(count_frequency("hello"))