'''
import random
n = random.randint(0,100)
i = 1

while i <=10:
	b = int(input("请输入数字:"))
	if n>b:
		print("猜小了")
	elif n<b:
		print("猜大了")
	else:
		print("猜中了")
		break	
	print("猜了%d次"%i)
	i+=1

'''
import random
n = random.randint(0,100)

for e in range(1,11):
	i =int(input("请输入1-100的整数:"))
	if i>n:
		print("猜大了")
	elif i<n:
		print("猜小了")
	else:
		print("猜中了")
		break
	print("猜了%d次"%e)
