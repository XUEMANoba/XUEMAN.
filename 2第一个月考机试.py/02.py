def hanshu(age):
	if age>0 and age<=2:
		print("婴儿")
	elif age>2 and age<=4:
		print("蹒跚学步")
	elif age>4 and age<=13:
		print("儿童")
	elif age>13 and age<=20:
		print("青少年")
	elif age>20 and age<=65:
		print("成年人")
	elif age>65:
		print("老年人")
	else:
		print("输入不合法")

age = int(input("请输入年龄"))
hanshu(age)
