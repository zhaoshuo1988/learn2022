'''IDLE开发环境中无法显示打印输出
'''
#导入模块 multiprocessing 多进程



import multiprocessing

import time

import os


#创建进程执行函数
def fun(sec,name):
    print('子进程{}函数开始执行……'.format(sec))
    for i in range(sec):
        #睡眠模拟程序执行
        time.sleep(3)
        print('My name is %s'%name)
    print(os.getppid(),'---',os.getpid())
    print('子进程{}函数执行完成'.format(sec))


#Windows系统下，必须把子进程相关代码放入if,linux 则不需要

if __name__=='__main__':
    #函数列表
    process_list =[1,2,3]
    name_list=['Lily','Tom','Jon']
    #回收列表
    jobs = []
    print('主进程开始执行……')
    #循环执行多进程
    for i in process_list:
        #创建子进程对象Process
        #trget:绑定执行目标函数
        #args :元组传参数
        #kwargs:字典传参
        #daemon=True 子进程随父进程而结束,需在star()前设置
        p =multiprocessing.Process(target = fun,
                                   kwargs={'sec':i,
                                           'name':name_list[i-1]})
        jobs.append(p)
        #启动子进程，并执行fun函数
        p.start()

    #循环回收进程
    for i in jobs:
        i.join
    print('主进程开始执行……')

    time.sleep(100)
'''
    print(multiprocessing.active_children())
    
    
    print(multiprocessing.active_children())

    #主进程模拟执行
    print('主进程开始执行……')
    print(multiprocessing.active_children())
    print(multiprocessing.current_process())
    sleep(2)
    print('主进程执行完成')
    


    #回收进程
    p.join()
'''
