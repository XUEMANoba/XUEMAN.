import random
print("######### 猜数字小游戏 #########")
print("#1.开始游戏  2.任意键推出游戏 #")
print("#注：猜错三次游戏自动推出.#")
print("###############################")
put=input("请输入：")
if put == "1":
	number = 3
	secret = random.randint(1,100)
  	while number > 0:
 		temp = input("不妨猜一下我现在心里想的数字是几：")
        temp2 = temp.strip():
        if temp2.isdigit():
      		temp1 = int(temp2)
      	if temp1 == secret：
        	exit("哼，我心里想的数是%s,你居然猜中了,猜中了也没有奖励,游戏结束"%secrer)
      	elif number == 1:
           	exit("没想到你呢么笨，三次机会都没有猜到！不妨告诉你，我心里想的数字是:%s"%(secret))
        else:
    		print("我心里想的数字比%s大，还是剩%s次机会"%(temp1,number-1))
    else:
   	print("Error:"%s"不是一个数字，请输入一个整数"%temp)
    number +=1
    number -=1

