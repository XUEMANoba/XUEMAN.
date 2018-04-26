movies=[{'name':'wang',"acter":'xiaoming','director':'huang','public_time':'2017'},{'name':'xiao',"acter":'xiaoming','director':'huang','public_time':'2017'}]
def add_movie():
    flag=True
    while flag:
        name= input("请输入要加入电影名:")
        movies_name=[]
        for item in movies:
            movies_name.append(item['name'])
        if name in movies_name:
            print("你添加的电影已收录!")
        else:
            flag=False
    acter=input("请输入主演:")
    director=input("请输入导演:")
    public_time=input("请输入公映时间:")
    movie_info={'name':name,'acter':acter,'director':director,'public_time':public_time}
    movies.append(movie_info)
    print("恭喜成功添加此电影")
def del_movie():
    flag = True
    while flag:
        name= input("请输入要删除的电影名:")
        movies_name=[]
        for item in movies:
            movies_name.append(item['name'])
        if name in movies_name:
            movies.pop(movies_name.index(name))
            print("删除成功")
            flag=False
        else:
            print("你删除的电影不存在")
def update_movie():
    flag = True
    while flag:
        name= input("请输入要修改的电影名:")
        movies_name=[]
        for item in movies:
            movies_name.append(item['name'])
        if name in movies_name:
            print("1:修改电影名".center(30, " "))
            print("2:修改主演".center(30, " "))
            print("3:修改导演".center(30, " "))
            print("4:修改公映时间".center(30, " "))
            index=movies_name.index(name)
            movies_dict={"1":'name',"2":"acter","3":'director',"4":'public_time'}
            choose=input('请选择操作:')
            if choose not in movies_dict:
                print('输入有误')
            movies[index][movies_dict[choose]]=input("请输入%s:" %movies_dict[choose])
            print("更新成功")
            flag=False
        else:
            print("你要修改的电影不存在")
def query_moives():
    flag = True
    while flag:
        name= input("请输入要查询的电影名:")
        movies_name=[]
        for item in movies:
            movies_name.append(item['name'])
        if name in movies_name:
            for i,s in movies[movies_name.index(name)].items():
                print ("%s:%s" %(i,s),end='\t')
            print('\t')
            flag=False
        else:
            print("你查询的电影不存在")
            print("你要修改的电影不存在")
def print_movies():
    while True:
        print("\033[32m欢迎来到电影管理平台\033[0m")
        print("1:新增电影".center(30, " "))
        print("2:修改电影".center(30, " "))
        print("3:查询电影".center(30, " "))
        print("4:删除电影".center(30, " "))
        print("5:退出操作".center(30, " "))
        choose_dict={"1":add_movie,"2":update_movie,"3":query_moives,"4":del_movie,"5":exit}
        choose=input("请选择操作：")
        if choose in choose_dict:
        	choose_dict[choose]()
        print("输入有误，请重新输入")
if __name__=="__main__":
    print_movies()
