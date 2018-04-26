print("计算闰平年小程序".center(30," "))
def hanshu():
	while True:
		a=int(input("选项1为输入年份，选项2为退出程序"))
		if a ==1:
			year = int(input("请输入年份:"))
			if (year%4==0 and year%100!=0) or year%400 ==0:
				print("是闰年")
			else:
				print("是平年")
		elif a ==2:
			break
		else:
			print("输入有误")
hanshu()
