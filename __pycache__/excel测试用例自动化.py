#1、excel测试用例读取 2、接口请求代码构建  3、测试结果写入到excel 4、后续辅助性工作

#excel包括：用例编号、用例名称、用例说明、接口地址、请求方式，请求头，请求参数，预期结果，返回结果,测试结果
import xlrd #第三方库 pip install xlrd///pip list查看所有库---读取excel表的库

#读取excel测试用例
excelDir = r'C:\Users\h\Desktop\1.xlsx'
#打开excel
workbook =xlrd.open_workbook(excelDir)
#查看所有的子表名
print(workbook.sheet_names()) #返回是list
workSheet = workbook.sheet_names()[1]
#或  workSheet = workbook.sheet_by_name('新增客户61个')
#读取一行
rows=workSheet.row_values(1)
print(rows)
#读取一列
clos = workSheet.cell_value(1)
#请求参数位于第一行第6列
#读取指定单元格,worksheet为表对象
cellData = workSheet.cell(1,6).value
print(cellData)

#print(workSheet.cell(1,6).ctype) #返回单元数据类型 0   1：字符串  2  3  4  5

#2、构建接口对应请求
import requests
import json
#获取token
token_url = 'http://47.96.181.17:9090/rest/ac01Controller'
token_data = {"userName":"3201903070064","password":"362387359"}
headers = {"Content-Type": "application/jason"}
resp = requests.post(token_url,data = json.dumps(token_data),headers=headers)
token = resp.json()['token']
print(token)
#获取返回状态码
# print('请求返回状态码---'，resp.status_code)
# #打印返回的内容
# print(resp.text) #字符串
# print('请求头---',resp.request.headers)
# print('请求body---',resp.request.body)

#新增用户
addUser_url = 'http://47.96.181.17:9090/rest/ac01Controller'
addUser_data = json.loads(cellData)  #请求参数--load可以直接转字典-------不懂
print(type(addUser_data))#---class dict----不懂
addUser_headers = {"Content-Type": "application/jason","X-AUTH-TOKEN":token} #令牌，服务器给的，用户名密码后就会给
addUser_resp = requests.post(addUser_url,data=json.dumps(addUser_data),headers=addUser_headers)
print(addUser_resp.text)

res= addUser_resp.json()['message']
if res =='成功':
    print('新增用户接口测试----成功，耗时---',addUser_resp.elapsed.total_seconds())
    excel_res = 'pass'
else:
    print('新增用户接口测试----失败')
    excel_res = 'fail'

#写回测试用例
#import xlutils
from xlutils.copy import copy
# 1 首先打开excel
#workbookWr  = xlrd.open_workbook(excelDir)
#2复制
workbookWr = copy(workbook)
wrSheet = workbllkWr.get_sheet(1)
wrSheet.write(1,9,excel_res)
workbookWr.save(r'C:\Users\h\Desktop\12.xlsx')







