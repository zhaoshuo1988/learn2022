# coding: UTF-8
import tkinter #导入相关的窗体模块
from tkinter import messagebox
class MainForm:  # 定义窗体类
    def __init__(self): #构造方法里进行窗体的控制
        self.root = tkinter.Tk()  # 创建一个窗体
        self.root.title('在制品管理系统')  #设置标题
        self.root.geometry("500x600")   #设置初始尺寸，字母x为小写
        self.root.maxsize(1000,800)  #设置最大尺寸
        self.root["background"] = 'pink'  #设置背景颜色
        
        #-------以下进行文本标签定义--------
        label_text =tkinter.Label(self.root, text="控制标签",
                bg="#123452",fg="#ff32fd",font=("微软雅黑",10))
        label_text.pack() #组件的布局，显示组件

        label_text.bind("<Button-1>", lambda event :
                self.event_handle(event,"Hello"))  #绑定处理事件

        
        self.root.mainloop()     #显示窗体

    def event_handle(self,event,info):  #事件处理方法
        
        text =tkinter.Text(self.root,width=100,height =30)
        text.insert("current","请输入正确的邮件信息")  #文本框提示信息
        text.bind("<Button-1>", lambda event:
                text.delete("0.0","end"))  #绑定事件，单机清除内容
        text.pack()  #动态添加组件

        tkinter.messagebox.showinfo(title = "信息提示",message=info)

def main(): # 主函数
    MainForm() #实例化窗体类

if __name__=="__main__":  #判断程序执行名称
    main()  # 调用主函数
