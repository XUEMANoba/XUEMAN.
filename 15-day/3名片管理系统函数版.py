print("欢迎使用名片管理系统".center(30,"*"))
cards = []
def print_menu():
	print("1:新增名片".center(30," "))
	print("2:修改名片".center(30," "))
	print("3:查询名片".center(30," "))
	print("4:打印全部名片".center(30," "))
	print("5:删除名片".center(30," "))
def input_fun():
	while True:
		fun_num = int(input("请选择功能:"))
		if fun_num ==1:
			add_card()
		elif fun_num ==2:
			update_card()
		elif fun_num ==3:
			check_card()
		elif fun_num ==4:
			print_card()
		elif fun_num ==5:
			del_card()
		else:
			print("输入有误请重新输入")
			continue
def add_card():
	card = {}
	print("新增名片")
	name = input("请输入名字:")
	flag = 0
	for temp in cards:
		if name == temp["name"]:
			flag = 1
			break
	if flag == 1:
		print("名字重复")
		return
	job = input("请输入职位:")
	company = input("请输入公司:")
	phone = int(input("请输入手机号:"))
	card["name"] = name
	card["job"] = job
	card["company"] = company
	card["phone"] = phone
	cards.append(card)
def update_card():
	print("修改名片")
	name = input("请输入修改名字:")
	flag = 0
	for temp in cards:
		if name == temp["name"]:
			flag = 1
	if flag ==1:
		print("1:修改名字".center(30," "))	
		print("2:修改职位".center(30," "))	
		print("3:修改公司".center(30," "))	
		print("4:修改手机号".center(30," "))	
		xuanze = int(input("请输入修改序号:"))
		if xuanze ==1:
			new_name = input("请输入新的名字:")
			temp["name"] = new_name
		elif xuanze ==2:
			new_job = input("请输入新的职位:")
			temp["job"] = new_job
		elif xuanze ==3:
			new_company = input("请输入新的公司名:")
			temp["company"] = new_company
		elif xuanze ==4:
			new_phone = int(input("请输入新的手机号:"))
			temp["phone"] = new_phone
		else:
			print("输入有误")
def check_card():
	name = input("请输入要查询的名字:")
	flag = 0
	for temp in cards:
		if name == temp["name"]:
			print("名字是%s\n职位是%s\n公司名是%s\n手机号是%d"%(temp["name"],temp["job"],temp["company"],temp["phone"]))
			flag = 1
	if flag ==0:
		print("查无此人\n")
def print_card():
	print("姓名\t职位\t公司\t联系方式")
	for temp in cards:
		print("%-12s%-12s%-12s%-12d"%(temp["name"],temp["job"],temp["company"],temp["phone"]))
def del_card():
	name = input("请输入要删除的名字:")
	flag = 0
	for temp in cards:
		if name == temp["name"]:
			flag =1
			sure = int(input("0确认删除1返回"))
			if sure ==0:
				cards.remove(temp)
				print("删除成功")
			break
		if flag ==0:
			print("没有此人")

print_menu()
input_fun()
