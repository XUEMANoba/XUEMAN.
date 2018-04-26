print("名片管理系统".center(30,"*"))
print("1:新增名片".center(30," "))
print("2:查找名片".center(30," "))
print("3:修改名片".center(30," "))
print("4:删除名片".center(30," "))
print("5:显示所有名片".center(30," "))
print("6:退出系统".center(30," "))
cards = []#定义空列表
while True:
	fun_number = int(input("请选择功能"))
	if fun_number == 1:
		print("新增")
		flag = 0 #默认值 0代表不在里边
		card = {} #定义空字典
		name = input("请输入名字")
		for temp in cards:
			if name == temp["name"]:
				flag = 1
				break
		if flag ==1:
			print("名字重复了")
			continue
		job = input("请输入职位")
		phone = int(input("请输入联系方式"))
		company = input("请输入公司名字")
		address = input("请输入公司地址")
		
		card["name"] = name
		card["job"] = job
		card["phone"] = phone
		card["company"] = company
		card["address"] = address
		cards.append(card)
		print("新增成功\n")

	elif fun_number == 2:
		name  = input("请输入要查的姓名")
		flag = 0#假设不在里面
		for temp in cards:
			if name == temp["name"]:
				flag=1
				print("姓名:%s\n职位:%s\n手机号:%s\n公司:%s\n公司地址:%s\n"%(temp["name"],temp["job"],temp["phone"],temp["company"],temp["address"]))
				break
			elif flag == 0:
				print("查无此人")
		#print("查找名片")
	elif fun_number == 3:
		name = input("请输入要修改的名字")
		for temp in cards:
			if name == temp["name"]:
				print("1:修改名字".center(30," "))
				print("2:修改职位".center(30," "))
				print("3:修改手机号".center(30," "))
				print("4:修改公司名称".center(30," "))
				print("5:修改公司地址".center(30," "))
				change_num = int(input("请选择修改序号"))
				if change_num ==1:
					name = input("请输入新的名字")
					temp["name"]=name
				elif change_num ==2:
					job = input("请输入新的职位")
					temp["job"]=job
				elif change_num ==3:
					phone = input("请输入新的手机号")
					temp["phone"]=phone
				elif change_num ==4:
					company = input("请输入新的公司名称")
					temp["company"]=company
				elif change_num ==5:
					address = input("请输入新的公司地址")
					temp["address"]=address
				else:
					print("输入有误")
		#print("修改名片")
	elif fun_number == 4:
		name = input("请输入你要删除的姓名")
		flag = 0#假设没有此人
		for temp in cards:
			if name == temp["name"]:
				flag = 1#找到了
				sure_num = int(input("0确认删除 1返回"))
				if sure_num == 0:
					cards.remove(temp)#删除
					print("删除成功")
				break
		if flag ==0:
			print("没有此人")
	elif fun_number ==5:
		print("姓名\t职位\t手机号\t公司名称\t公司地址")
		for temp in cards:
			print("%-12s%-12s%-12s%-12s%-12s"%(temp["name"],temp["job"],temp["phone"],temp["company"],temp["address"]))

	else:
		sure_num = int(input("0确认退出 1返回"))
		if sure_num ==0:
			print("退出成功")
			break
		else:
			continue
