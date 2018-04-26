cards = [] #定义空列表
def print_movies():
	while True:	
		print("\033[32m欢迎来到电影管理平台\033[0m")
		print("1:新增电影".center(30, " "))
		print("2:修改电影".center(30, " "))
		print("3:查询电影".center(30, " "))
		print("4:删除电影".center(30, " "))
		print("5:退出操作".center(30, " "))
		fun_num = int(input("请选择功能:"))
		if fun_num ==1:
			add_movie()
		elif fun_num ==2:
			update_movie()
		elif fun_num ==3:
			query_movie()
		elif fun_num ==4:
			del_movie()
		elif fun_num ==5:
			print("退出成功")
			break
		else:
			print("输入有误请重新输入")
			continue

def add_movie():
	card = {}  #定义空字典
	flag = 0  #默认不在里边
	name = input("请输入电影名字:")
	for temp in cards:  #遍历列表 
		if name == temp["name"]:
			flag = 1
			break
	if flag ==1:
		print("名字重复录入")
		return
	cter=input("请输入主演:")
	director=input("请输入导演:")
	public_time=int(input("请输入公映时间:"))
	card["name"] = name
	card["cter"] = cter
	card["director"] = director
	card["public_time"] = public_time
	cards.append(card)
	print("成功录入")

def update_movie():
	name = input("请输入修改名字:")
	flag = 0
	for temp in cards:
		if name == temp["name"]:
			flag = 1
	if flag ==1:
		print("1:修改电影名字".center(30," "))	
		print("2:修改主演".center(30," "))	
		print("3:修改导演".center(30," "))	
		print("4:修改公映时间".center(30," "))	
		xuanze = int(input("请输入修改序号:"))
		if xuanze ==1:
			new_name = input("请输入新的电影名字:")
			temp["name"] = new_name
		elif xuanze ==2:
			new_cter = input("请输入新的主演:")
			temp["cter"] = new_cter
			print("更新成功")
		elif xuanze ==3:
			new_director = input("请输入新的导演:")
			temp["director"] = new_director
		elif xuanze ==4:
			new_public_time = int(input("请输入新的公映时间:"))
			temp["public_time"] = new_public_time
		else:
			print("输入有误")


def query_movie():
	name = input("请输入要查询的名字:")
	flag = 0
	for temp in cards:
		if name == temp["name"]:
			print("电影名字:%s\n主演:%s\n导演:%s\n公映时间:%d\n"%(temp["name"],temp["cter"],temp["director"],temp["public_time"]))
			flag = 1
	if flag ==0:
		print("没有此电影")


def del_movie():
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
			print("没有此电影")

print_movies()

