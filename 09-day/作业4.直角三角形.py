'''
i = 1
for e in range(1,6):
	if i==e:
		print("*"*i,end="")
	i+=1
	print("")
'''

for i in range(5):
	for j in range(1,i+1):
		print("*",end="")
	print("")
