account = input("请输入账号")
pwd = input("请输入密码")
name = input("请输入名字")
money1 = 100000#原有存款
money2 = input("请输入要取金额")
yu_e = money1-int(money2)
print("账号:%s\n密码:%s\n名字:%s\n原有存款:%d\n要取金额:%s\n剩余:%d"%(account,pwd,name,money1,money2,yu_e))
