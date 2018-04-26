while True:
	num = int(input("请输入1注册2登录"))
	if num ==1:
		register()
	elif num ==2:
		login()
	else:
		print("输入错误")
list=[]
def register():
	account = int(input("请输入注册账号"))
	pwd = int(input("请设置密码"))
	flag = 0
	for i in list:
		if account == i["account"]:
			print("账号已存在")
			flag = 1
	if flag ==0:
		dict = {}
		dict["account"] = account
		dict["pwd"] = pwd
		list.append(dict)
		print("注册成功")
def login():
	account = int(input("请输入注册账号"))
	pwd = int(input("请设置密码"))
	flag = 0
	for i in list:
		if account = i["account"]:
			if i.get(status) = 1:
				print("账号在登录着")
			else:
				if pwd = i["pwd"]:
					print("登录成功")
					i["status"] = 1
				else:
					print("登录失败")
			flag = 1
			break
	if flag ==0:
		print("账号不存在请先注册")




