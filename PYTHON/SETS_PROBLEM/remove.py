""" this method is basically remove all the occurence of the existing element from the set if it is present,
but, if it is not present then print the original set"""

s = {1,5,7,6,1,8,6}
s.discard(10)
print(s)