name = 12345
pwd = 12345

s_name = int(input("请输入用户名:"))
s_pwd = int(input("请输入密码:"))

if s_name == name and s_pwd == pwd:
	print("欢迎来到王者荣耀")
else:
	print("用户名或密码错误")
