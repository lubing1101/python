# -*- coding:utf-8 -*-
import urllib,re,xlwt
def get_content():
    url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    a = urllib.urlopen(url)
    html = a.read()
    html = html.decode('gbk') #decode解码
    #print html
    return html
#匹配内容
def get():
    html = get_content()
    reg = re.compile(r'class="t1 ">.*?<a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>',re.S) #编译为正则表达式对象
    items = re.findall(reg,html)
    #print items [0][0]
    return items
#创建表格
def excel_write(items):
    newTable = '20170331.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('20170331.sheet')
    headData = ['招聘职位','公司','地址','薪资','日期']
    for column in range(0,5):
        ws.write(0,column,headData[column],xlwt.easyxf('font:bold on'))
    index = 1
    for item in items:
        for i in range(0,5):
            #print item[i]
             ws.write(index,i,item[i])
        index+=1
        wb.save(newTable)
if __name__ == "__main__": #判断文件入口
    items = get()
    excel_write(items)




