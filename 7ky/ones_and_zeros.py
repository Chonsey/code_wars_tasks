def binary_array_to_number(arr):
    num = 0
    index = 0 
    for i in reversed(arr):
        num += i * (2 ** index)  
        index += 1 
    return num
