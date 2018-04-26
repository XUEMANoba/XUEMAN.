while True:
	x = int(input("请输入一个数字:"))
	y = int(input("请输入一个数字:"))
	sum = 0

	if x<y:

		for n in range(x,y+1):
			sum+=n
		
		print(sum)
		break
	else:
		print("输入有误")
	
	










'''
sum1 = 0
while x <= y:
	sum1+=x
	x+=1
	print(sum1)
'''

