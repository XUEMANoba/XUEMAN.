list = [13,6,10,21,30,50,4,89,2]
for i in range(len(list)):
	for j in range(i+1,len(list)):
		if list[i] > list[j]:
			list[i],list[j] = list[j],list[i]
print(list)

num = 4
center = int(len(list)/2)

if num in list:
	while True:
		if list[center] > num:
			center = center-1
		elif list[center] < num:
			center = center+1
		elif list[center] == num:
			print("要找的数字是%d索引是%d"%(num,center))
			break
