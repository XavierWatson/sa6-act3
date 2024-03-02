import random
numbers = [1,2,3,4,5,6]
n = random.randint(0,4)
expo_mapping = list(map(lambda x:x**n ,(numbers)))
print(f'n={n} {expo_mapping}')