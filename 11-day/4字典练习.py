information = {"name":"娄雪嫚","age":"17","sex":"女","group":"汉"}
print(information)

#所有的键
print(information.keys())
#所有的值
print(information.values())
#键对值形式返回
print(information.items())

#增加
information["place"] = "河南省"
information["merry"] = "未婚"
information.setdefault("age",18)
information.setdefault("height",170)
print(information)

#删除
information.pop("merry")
information.popitem() #随即删除一个
#information.clear()
#del information["age"]

#改
information["name"] = "雪漫"

#查
print(information["name"])
#print(information["merry"])没有这个键会报错
print(information.get("merry"))

#合并
information_2 = {"name":"雪嫚","weight":"110"}
information.update(information_2)
print(information)

