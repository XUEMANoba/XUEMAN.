list = []
all_count = 0#坐的次数
def my_input():
	dict = {} #月份和钱
	sum = 0#记录每月花多少钱
	global all_count #声明要修改变量
	month = int(input("请输入月份"))
	if month <= 0 or month > 12:
		print("输入有误")
		return 
	count = int(input("请输入每天做地铁的次数"))
	if count <= 0:
		print("次数输入有误")
		return
	distance = float(input("请输入距离"))
	if distance <= 0:
		print("距离输入有误")
		return
	all_count+=30*count
	for i  in range(1,30*count+1):
		if  distance <= 6:
			money = 3
		elif distance > 6 and distance <=12:
			money = 4
		elif distance > 12 and distance <=22:
			money = 5
		elif distance > 22 and distance <=32:
			money = 6
		elif distance > 32: 
			if (distance - 32)%20 == 0:
				money = 6 + (distance-32)/20
			else:
				money = 6+ int((distance-32)/20) + 1

		if sum >= 100 and sum < 150: 
			money = money * 0.8
		elif sum>=150 and sum < 400:
			money = money * 0.5
		
		sum = sum+money
	dict[month] = sum		
	list.append(dict)
	print(list)


def cal_sum():
	all_sum = 0
	for i in list:
		for k,v in i.items():
			all_sum+=v
			print("%d月花了%.02f元"%(k,v))
	print("总共花了%.02f"%all_sum)
	print("总共坐了%d次"%all_count)


while True:
	fun = int(input("1:继续乘坐 2:计算"))
	if fun == 1:
		my_input()
	else:
		cal_sum()
