list = []
def wangzhe(hero):
	list.append(hero)


while True:
	if len(list) == 5:
		print(list)
		break

	name = input("请输入英雄名字")
	wangzhe(name)
