def register(phone,pwd):
	result = diao(phone)
	if result:
		print("注册成功")
	else:
		print("注册失败")


def login(phone,pwd):
	result = diao(phone)
	if result:
		print("登录成功")
	else:
		print("登录失败")

def diao(phone):
	if phone.startswith("1") and len(phone) == 11:
		return True
	else:
		return False


register("11111","22222")
login("11111","22222")
