list = []
def register():
	account,pwd = cus_input()
	flag =0
	for i in list:
		if account == i["account"]:
			print("账号已存在")
			flag=1
			break
	if flag == 0:
		dict = {}
		dict["account"] = account
		dict["pwd"] = pwd
		list.append(dict)
		print("注册成功")



def login():
	account,pwd = cus_input()
	flag = 0
	for i in list:
		if account ==i["account"]:
			if i.get("status") ==1:
				print("在登录")
			else:
				if pwd ==i["pwd"]:
					print("登陆成功")
					i["status"] = 1
				else:
					print("登录失败")
			flag = 1
			break
	if flag == 0:
		print("账号不存在请先注册")
def loginout():
	account,pwd = cus_input()
	flag = 0
	for i in list:
		if account ==i["account"]:
			if i.get("status") ==1:
				print("退出成功")
				i.get("status") ==0
			else:
				print("账号没登录")
			flag = 1
			break
		if flag ==0:
			print("账号不存在")
def cus_input():
	account = input("请输入账号:")
	pwd = input("请输入密码:")
	return account,pwd
while True:
	fun = int(input("请选择功能:1=注册,2=登录"))
	if fun ==1:
		register()
	elif fun ==2:
		login()
	elif fun ==3:
		loginout()
