def find_max(array,parameter):
    maximum = list(sorted(array, key=parameter))
    return maximum[-1]
numbers = [1,45,99999,34,5311,4224,66,2]
param = lambda x:x

print(find_max(numbers,param))