import time
from random import randit
list = []
#入职
def add_user():
	dict = {}
	name = input("请输入员工姓名")
	flag = 0#默认不在里边
	for i in dict:
		if name in i["dict"]:
			dict.append(i["name"])
			flag = 1
	if flag ==1:
		print("重复输入")
	num = int(input("请输入工号"))
	age = int(input("请输入年龄"))
	job = input("请输入工作岗位")
	salary = input("请输入每月薪水")
	creat._time = randint(0,1524190943)
	dict["name"] = name
	dict["num"] = num
	dict["age"] = age
	dict["job"] = job
	dict["salary"] = salary
	list.append(dict)
	print("添加成功")
#查询
def query_user():
	name = input("请输入名字")
	for temp in list:
		if name == temp["name"]:
			print("名字是:%s"%name)
			now = int(time.time())
			diff = now - temp["create_time"]
			day = diff / 86400
			print("薪水%f"%(temp["salary"]/30*day))
			break

#离职
def out_company():


def menu():
	print("员工管理系统".center(30,"*"))
	print("1.员工入职")
	print("2.查询信息")
	print("3.员工离职")

def fun_input():
	while True:
		showMenu()
		fun = int(input("请选择功能"))
		if fun == 1:
			add_user()
		elif fun == 2:
			query_user()
		elif fun == 3:
			out_company()

fun_input()			

