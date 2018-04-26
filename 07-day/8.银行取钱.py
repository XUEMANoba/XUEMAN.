#银行取钱
account = 20010301
pwd = 596
z_money = 1000

s_account = int(input("请输入账号:"))
s_pwd = int(input("请输入密码:"))
if s_account == account and s_pwd == pwd:
	print("开始取钱")
	money_q = float(input("请输入取钱金额:"))
	if money_q > z_money:
		print("没钱取毛线")
	elif money_q < z_money:
		print("取了%.02f元，还剩%.02元"%(money_q,z_money-money_q))
elif s_account != account and s_pwd != pwd:
	print("非法账户")
