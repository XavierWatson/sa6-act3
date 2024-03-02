list1=['a','d','e','f','h','j']
list2=['a','b','f','c','h']

interlist = list(filter(lambda x: x in list1, list2))
print(interlist)