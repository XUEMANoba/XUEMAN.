'''
list = [1,2,3,4,5,6,7,8,9]
for i in list:
	list.remove()
	print(list)
'''


list = [1,2,3,4,5,6,7]
for i in range(len(list)-1,-1,-1):
	list.pop(i)
print(list)


list = [1,2,3,4,5,6,7]
for i in list[:]:
	list.remove(i)
print(list)
