acc = "123456"
pwd = "123456"
print("TI MI")
choose_login = input("请选择登录方式:1=qq，2=微信，3=输入账号密码")

if choose_login =="1":
	print("qq登录成功")
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

elif choose_login == "2":
	print("微信登录成功")
elif choose_login == "3":
	account = input("请输入账号:")
	pwd = input("请输入密码:")
	if account == acc and pwd == pwd:
		print("账号登录成功")
	else:
		print("登录失败")
