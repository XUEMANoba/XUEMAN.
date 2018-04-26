void main()  
{  
  
    const int index = 5;  
    struct student  
    {  
        char name[4];  
        int mark1;  
        int mark2;  
        int mark3;  
      
        void setName(char c[])  
        {  
            char *nameip = name;  
            for (int i=0;i<sizeof(c);i++)  
            {  
                *(nameip+i) = c[i];  
                //std::cout <<name[i];  
            }  
        }  
        void showName()  
        {  
            for(int i=0;i<sizeof(name);i++)  
            {  
                std::cout <<name[i];  
            }  
              
        }  
  
        int getCmark(){  
            return (mark1+mark2+mark3)/3;  
        }  
    };  
    struct student stu[index];  
  
      
    char ip[20] ;  
  
    for (int i=0;(i<index);i++)  
    {  
        std::cout <<'\n';  
        std::cout <<"请输入学生姓名：";  
  
        std::cin >>ip;  
        std::cout <<'\n';  
        stu[i].setName(ip);  
        std::cout <<"请输入科目一成绩：";  
        std::cin >>stu[i].mark1;  
        std::cout <<'\n';  
        std::cout <<"请输入科目二成绩：";  
        std::cin >>stu[i].mark2;  
        std::cout <<'\n';  
        std::cout <<"请输入科目三成绩：";  
        std::cin >>stu[i].mark3;  
        std::cout <<'\n';  
    }     
      
    int j = 0;  
    using namespace std;  
    for (int i =j;i<index;i++)  
    {  
          
        //cout << stu[i].getCmark();  
        if (stu[i].getCmark() < stu[i+1].getCmark())  
        {  
            j = i+1;  
        }  
          
    }  
    std::cout <<"成绩最高的学生名字:";  
    stu[j].showName();  
    std::cout<<'\n';  
    std::cout <<"平均成绩是:";  
    std::cout <<stu[j].getCmark();  
    std::cout<<'\n';  
}
