list = [1,3,5,7,9,11,13,15,17,19]

num = 9
center = int(len(list)/2)

if num in list:
	while True:
		if list[center] > num:
			center = center - 1
		elif list[center] < num:
			center = center + 1
		elif list[center] == num:
			print("要找的数字是%d在索引%d"%(num,center))
			break
