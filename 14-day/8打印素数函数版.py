def hanshu(x,y):

	for i in range(x,y+1):
		a = 0
		for j in range(2,i):
			if i%j == 0:
				a = 1
				break
		if a == 0:
			print(i)
hanshu(100,200)
