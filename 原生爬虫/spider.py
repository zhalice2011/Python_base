#coding:utf-8
#模拟请求的库
from urllib import request 
import ssl
import re
#断点调试
ssl._create_default_https_context = ssl._create_unverified_context

#第一步模拟http请求
class Spider():
    url='https://www.panda.tv/cate/lol'
    root_patten = '<div class="video-info">([\w\W]*?)</div>' 
    name_patten = '</i>([\s\S]*?)</span>'
    rank_patten = '<span class="video-number">([\s\S]*?)</span>'
    #定义一个函数获取内容  __表示私有方法
    def __fetch_content(self):
         r = request.urlopen(Spider.url) #此方法可以接受一个url
         htmls = r.read()                #用read方法读取url 但是取到的值是二进制的byte的数组
         htmls = str(htmls, encoding='utf-8')  #替换成html文件
         return htmls
         #print(r.read().decode('utf-8'))
        #print(htmls) 
    #分析网页的方法
    def __analysis(self,htmls):
        root_html = re.findall(self.root_patten,htmls)
        anchors = []
        for html in root_html:
            name = re.findall(self.name_patten,html)
            rank = re.findall(self.rank_patten,html)
            anchor = {'name':name,'rank':rank}#用字典(obj)的方式把name和rank都装ame进去
            anchors.append(anchor)            #push到上面的列表(数组)
        #print(anchors)
        return anchors

    #精炼我们的数据
    def __refine(self,anchors):
        l = lambda achor:{'name':achor['name'][0].strip(),'rank':achor['rank'][0]}
        return map(l,anchors)
    #对数据进行排序    
    def __sort(self,anchors):
        anchors = sorted(anchors, key = self.__sort_seed,reverse=True)
        return anchors

    #需要返回一个可以支持比较运算的  也就是人数
    def __sort_seed(self,anchor):
        print("anchor['rank']",anchor['rank'])  #anchor['rank'] 442.8万
        r = re.findall('\d+\.?\d*',anchor['rank'])  #字符串 "1.2"
        print('r',r)
        number = float(r[0])  #数字 "1.2"
        #判断如果里面有万的这个字
        if '万' in anchor['rank']:    
            number*=10000
        print("最终的number",str(number))
        return number

    #展现我们的数据
    def __show(self,anchors):
        for rank in range(0,len(anchors)):
            print('排名:'+str(rank+1) )
                print(rank+anchor['name']+'--------->'+anchor['rank'])
        #for anchor in anchors:
            

    def go(self):
        htmls = self.__fetch_content()     #提取html  
        anchors = self.__analysis(htmls)   #粗炼
        anchors = list(self.__refine(anchors))  #精炼---->变成我们要的数据结构  
        ancho = self.__sort(anchors)  #排序
        self.__show(ancho)  #展现


#实例化spider
spider = Spider()

spider.go()