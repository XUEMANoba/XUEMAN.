account = 123456
pwd ="abc"
account_1 = int(input("请输入微信号:"))
pwd_1 = input("请输入微信密码:")

if account_1 == account and pwd_1 == pwd:
	print("登录成功")
elif account_1 != account:
	print("账号错误")
elif pwd_1 != pwd:
	print("密码错误")
