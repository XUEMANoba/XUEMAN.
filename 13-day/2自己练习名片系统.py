print("名片管理系统".center(30,"*"))
print("1.添加名片".center(30," "))
print("2.查找名片".center(30," "))
print("3.修改名片".center(30," "))
print("4.删除名片".center(30," "))
print("5.退出系统".center(30," "))
list[]
while True:
	fun_number = int(input("请选择功能"))
	if fun_number == 1:
		print("新增")
		flag = 0
		
