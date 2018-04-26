print("欢迎使用计算器".center(30," "))

def jisuanqi(q,w,e):
	if e == "+":
		a = q+w
		return a
	elif e == "-":
		a = q-w
		return a
		#print("差是%.02f"%a)
	elif e == "*":
		a = q*w
		return a
	elif e == "/":
		if w == 0:
			print("输入有误")
		else:
			a = q/w
			return a
while True:
	x = float(input("请输入一个数字"))
	y = float(input("请输入一个数字"))
	z = input("请输入+-*/")
	jieguo = jisuanqi(x,y,z)
	print(jieguo)
