#爬虫

import requests as rqs
from lxml import etree      #引入lxml库中etree
a=rqs.get("http://www.douban.com",params={'q':'python'})    #params={dict}传参访问

'''http请求类型   GET:向特定资源发出请求
               POST:向指定资源提交数据进行处理请求（例如提交表单
                   或上传文件）。数据被包含在请求体中
                PUT：向指定资源位置上传其最新内容
                DELETE:请求服务器删除Reques-URL所表示的资源
                HEAD:只请求页面的首部
                OPIONS:允许客户端查看服务器性能'''

a.encoding='utf-8'  #设置解码编码
text=a.text              #解码为文本文件
content=a.content           #以解码为二进制文件，常用与图片

b=rqs.post('https://www.douban.com',data={'user':'riyueguanghua','password':'12345678'},
           headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36_ (KHTML, \
                     like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE/10.0.2158.0'})
            #提交表单，data={dict}
            #headers={dict}模拟浏览器头部信息，反爬虫
            #coookies={dict}提交cookie内容
            #timeout=3 超时中断'
            #proxies={dict} 代理IP地址{'http':'http://10.1.10.12:80'}（代理列表可写入多个IP地址）

b.status_code
'''查看请求是否成功,request.codes.ok 查询成功的代码
            HTTP状态码：
            成功（2字头）：代表请求已成功被服务器接收，理解、并接受[1],比如200代表OK
            重定向（3字头），301重定向r.history
            请求错误（4字头）：代表客户端看起来可能发生了错误，妨碍了服务器的处理。
            服务器错误（5、6字头）：服务器在处理请求过程中有错误或异常状态发生。
'''
会话=rqs.session() #建立会话,会话可以有get,post等方法
bd=rqs.get('http://www.baidu.com/', headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36_ (KHTML, \
                     like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE/10.0.2158.0'})
bd.encoding='utf-8'
html=etree.HTML(bd.text)
num1=html.xpath('//*[@id="u1"]/a[1]/text()')[0]#提取文本信息
h1=html.xpath('////*[@id="u1"]/a[1]/@href')     #提取标签内连接属性
print(num1,h1)
pic=html.xpath('//*[@id="lg"]/img[1]/@src')     #lg提取网址属性
print(pic)
pic_=rqs.get('http:'+ pic[0],headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36_ (KHTML, \
                     like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE/10.0.2158.0'})
with open ('baidu.png','wb')as f:                 #新建文件
    f.write(pic_.content)                       #以二进制写文件

    

    
            



