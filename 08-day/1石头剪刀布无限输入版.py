'''
1=石头
2=剪刀
3=布
'''
num = 0
num_1 = int(input("请输入玩的次数:"))
import random
while num < num_1:
	player = int(input("请输入1--石头2--剪刀3--布"))
	computer = random.randint(1,3)

	if (computer==1 and player==2) or (computer==2 and player==3) or (computer==3 and player==1):
		print("你输了")
	elif computer == player:
		print("真默契")
	else:
		print("你赢了")
	num+=1
	print("玩了%d次"%num)
