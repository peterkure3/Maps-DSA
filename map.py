#MAPS
#Python program that implements maps using dual list

# keys
# This will be stored in listA
listA = ['one','two', 'three']

# values
# listB holds the values
listB = ['Cricket', 'Football', 'Wrestling']

# map function creates a new array for every element of a calling function.

# output
print(list(map(lambda x, y: x +' '+ y, listA, listB)))