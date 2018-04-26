print("欢迎使用电影院订票系统",center(30,"*"))
card = []
def menu():
	print("1.我要订票",center(30," "))
	print("2.电影改签",center(30," "))
	print("3.查询电影",center(30," "))
	print("4.打印电影票",center(30," "))
	print("5.退票",center(30," "))

def choose_num():
	while True:
		input_num = ("请选择功能:")
		if input_num == 1:
			add_movie()
		elif input_num == 2:
			revise_movie()
		elif inpue_num == 3:
			search_movie()
		elif input_num == 4:
			print_movie()
		elif input_num == 5:
			return_ticket()
		else:
			print("输入有误请重新输入")
			break
def add_movie():
	cards = {}
	print("我要订票",center(30,"*"))
	print("1后来的我们",center(30," "))
	print("2.头好玩家",center(30," "))
	print("3.脱单告急",center(30," "))
	print("4.覆灭",center(30," "))
	print("5.犬之岛",center(30," "))
	print("6.毕业作品",center(30," "))
	name = input("请输入电影名字:")
	flag = 0
	if fun_num == 1:


	


def revise_movie():
	print("电影改签")
	print("1修改场次")
	print("2修改时间")



menu()
choose_num()
