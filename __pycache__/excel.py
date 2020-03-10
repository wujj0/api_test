import xlrd
import xlwt
'''
def readexce():
    workbook=xlrd.open_workbook(r'E:\哈哈.xls')
    print(workbook.sheet_names())
    sheet2=workbook.sheet_by_name('A')
    nrows=sheet2.nrows
    ncols=sheet2.ncols
    print(nrows,ncols)

    cell_A=sheet2.cell(1,1).value
    print(cell_A)

if __name__=='__main__':
    readexce()

stus = [['年','月'], ['2018', '10'], ['2017', '9'], ['2016', '8']]
#stus = [['年', '月'], ['2018', '10'], ['2017', '9'], ['2016', '8']]
Excel=xlwt.Workbook()
sheet =Excel.add_sheet('B')
row=0
for stu in stus:
    col=0
    for s in stu:
        sheet.write(row, col, s)
        col=col+1
    row=row+1
Excel.save('111.xls')
'''

import unittest
from python.register_new.register import register
from python.register_new.register_testcase_new import RegisterTestCase
from HTMLTestRunnerNew import HTMLTestRunner
class RegisterTestCase(unittest.TestCase):
     # 初始化测试用例
    def __init__(self,modethod_name,excepted,data):
       # modethod_name 测试用例方法名
        super().__init__(modethod_name)
         # excepted 测试用例的预期结果
        self.excepted = excepted
        # data 测试用例参数值
        self.data = data

    def setUp(self):
        print("准备测试环境，执行测试用例之前会执行此操作")

    def tearDown(self):
        print("还原测试环境，执行完测试用例之后会执行此操作")

    def test_register(self):
        res = register(*self.data)
        try:
            self.assertEquals(self.excepted,res)
        except AssertionError as e:
            print("该条测试用例执行未通通过")
            raise e
        else:
            print("该条测试用例执行通过")

 # 创建测试套件
suite = unittest.TestSuite()

 # 将测试用例添加至测试套件中
case = [{'excepted':{"code": 1, "msg": "注册成功"},'data':('python1', '123456','123456')}, {'excepted':{"code": 0, "msg": "两次密码不一致"},'data':('python1', '1234567','123456')}]
for case in cases:
    suite.addTest(RegisterTestCase('test_register',case['excepted'],case['data']))

 # 执行测试套件，生成测试报告
with open("report.html",'wb') as f:
    runner = HTMLTestRunner(
        stream = f,
         verbosity = 2,
         title = 'python_test_report',
         description = '这是一份测试报告',
         tester = 'WL'
    )
    runner.run(suite)