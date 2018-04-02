1=石头
2=剪刀
3=布
player = int(input("请输入1--石头2--剪刀3--布"))
import random
computer = random.randint(1,3)

if (computer==1,player==2) or (computer==2,player==3) or (computer==3,player==1):
	print("你输了")
elif computer == player:
	print("真默契")
else:
	print("你赢了")
