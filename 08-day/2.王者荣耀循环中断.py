acc = "123456"
pwd = "123456"
print("TI MI")
num = True

while num:
	s_acc = input("请输入账号:")
	s_pwd = input("请输入密码:")
	if s_acc == acc:
		print("登录成功")
		xzyx = int(input("请选择英雄 1=射手2=法师3=刺客4=坦克5=辅助"))

		if xzyx == 1:
			print("太阳的后裔")
		if xzyx == 2:
			print("最美的貂蝉")
		if xzyx == 3:
			print("暴力美猴王")
		if xzyx == 4:
			print("免费的亚瑟")
		if xzyx == 5:
			print("绿头发庄周")
	else:
		print("重新输入密码")
		num+=1
		if num > 3:
			print("错误次数太多")
			break



	'''
	elif choose_login == "2":
		print("微信登录成功")
	elif choose_login == "3":
	'''
