#接口测试自动化
#先列出课程，再添加课程，再列出课程，再检查是否多了添加的
#列出课程
import requests
from pprint import pprint#打印的库，为了打印好看

res = requests.get('http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20')

list1 = res.json()['retlist']
#if res.status_code==200:
#    print('测试通过')
#else:
#    print('测试不通过')
# print(res.status_code)
# print(res.json())
# pprint(res.json(), width=30)#分行显示

#增加课程
#post,其中{}代表是表单
#三个引号是因为要换行，就不用了\n了，引号中间的{}是字符串
#这个请求之后页面上就多了一条数据
res = requests.post('http://localhost/api/mgr/sq_mgr/',
              data={
                  'action':'add_course',
                  'data':'''{   
    "name":"hah",
    "desc":"初中化学课程"
}
'''
              })
retObj = res.json()
pprint(res.json(), width=30)
#返回的{'id':1419,'recode':0}
if retObj['recode'] ==0:
    print("检查点==> 返回结果retcode为0，检查通过")
else:
    print("检查点==> 返回结果retcode不为0，检查不通过")


res = requests.get('http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20')

list2 = res.json()['retlist']

newcourse = None

for one in list2:
    if one not in list1:
        newcourse = one
        break

assert newcourse !=None
assert newcourse['name'] == '1'
assert newcourse['id'] == '2'

print(' =====test case pass====')
 




#返回json格式的消息体，
# {
#     "retlist":[
#         {
#             "name":"初中语文"，
#             "id":400
#         },
#         {
#             "name":"初中数学"，
#             "id":400
#         }
#     ],
#     "total":2,
#     "retcode":0
# }



