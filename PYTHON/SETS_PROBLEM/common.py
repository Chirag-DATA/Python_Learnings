lst1 = [1,2,3,4,5,6]
lst2 = [4,5,6,7,8]
lst3 = [4,5,9,10]

#typecasting
s1 = set(lst1)
s2 = set(lst2)
s3 = set(lst3)

common = (s1.intersection(s2)).intersection(s3)
print(f'The common elements in three lists are {common}')

'''The second method is by using the following code: (s1 & s2 & s3)'''
