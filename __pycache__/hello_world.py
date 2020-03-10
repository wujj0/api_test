message="hello"
print(message)
message="hello world"
#首字母大写
print(message.title())  
#全部大写
print(message.upper())
#全部小写
print(message.lower()) 
#合并字符串
first_name="a"
last_name="b"
full_name=first_name + " " + last_name
print(full_name)
print("hello, "+ full_name.title() + "!")
#使用制表符或换行符添加空白
print("language:\n\tpython\n\tC")
#删除空白--------失败
fav_language = " python "
fav_language.lstrip()
print("1" + fav_language +"2")
#整数-----失败
3/2
3**2
0.1+0.1
#str
age=20
message="a" + str(age)+ "b"
print(message)

#列表
bicyles=['trek', 'redline', 'cannonale']
print(bicyles)
#访问第一个元素
print(bicyles[0].title())
#最后一个
print(bicyles[-1])
#修改元素
bicyles[0]='tac'
print(bicyles)
#添加元素
bicyles.append('ducati')
print(bicyles)
#插入元素
bicyles.insert(1,'duca')
print(bicyles)
#空列表
cycles=[]
#删除元素
del bicyles[1]
print(bicyles)
#使用pop删除元素，访问被删除的值
poped_bicyles=bicyles.pop()
print(bicyles)
print(poped_bicyles)
#弹出列表中任何位置处的元素
a=bicyles.pop(1)
print(a)
#根据值删除元素
bicyles.remove('cannonale')
print(bicyles)

#组织列表
#排序(永久)
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
#相反排序
cars.sort(reverse=True)
print("相反排序:")
print(cars)
#临时排序
print("临时排序")
print(sorted(cars))
print(cars)
#倒着打印列表(永久)
print("倒着打印")
cars.reverse()
print(cars)#print前面不要缩进
#确定列表长度-------失败
len(cars)

print("-------------------------------")
#遍历整个列表
magicians=['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ",that was a great trick")
    print("I can't wait to see your next trick\n") 
print("thank you")

#创建数值列表(全部列表)
for value in range(1,5):
    print(value)

#创建数字列表
numbers =list(range(2,11,2))
print(numbers)

squares=[]
for value in range(1,11):
    square = value **2
    squares.append(square)
print(squares)  

#列表计算--------------失败
digits=[1,2,3,4,5]
sum(digits)
max(digits)

#列表解析
squares=[value**2 for value in range(1,11)]
print(squares)

#处理列表部分元素
#切片
players=['charles','martina','michael','eli']
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])#最后三个

for player in players[:3]:
    print(player)

#复制列表
my_foods=['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(friend_foods)

#两个列表变的一样
my_foods=['pizza','falafel','carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

#定义元组(元组是不可变的列表)----------失败
#dimensions=（200,50）
#print(dimensions[0])
#print(dimensions[1])
#错误的：dimensions[0]=250

#修改元组变量
#dimensions = (200,50)
#for dimension in dimesions:
   # print(dimension)
#dimensions = (400,100)
#for dimension in dimensions:
  #  print(dimension)

  #遍历元组中的所有值
 # dimensions = (200,50)
#for dimension in dimesions:
   # print(dimension)

#条件测试
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#检查是否相等-----------失败
car='bmw'
car=='bmw'#返回true或false

car='Audi'
car=='audi'  #返回false
car.lower=='audi' #返回true

#检查不相等
a='mushrooms'
if a!='anchovies':
    print('aaaa')

#比较数字
age=18
age==18  #返回true
if age!=40:
    print('bbbb')

#检查多个条件
age_0=22
age_1=18
age_0 >= 21 and age_1 >=21  #返回false
(age_0 >= 21) or (age_1 >=21) #返回true

#检查特定值是否在列表中
a=['q','w','e']
'q' in a  #返回true
b='d'
if b not in a:
    print('ddddd')
    print('eeeee')
else:
    print('yyyyyyy')

#if-elif-else，检查两个用这个，上面的是检查一个,if没有通过就执行下一个
age=12
if age <4:
    print("$0")
elif age <18:
    print("$5")
elif age <65:
    print("$10")
else:
    print("$5")
#省略else
age=12
if age <4:
    print("$0")
elif age <18:
    print("$5")
elif age <65:
    print("$10")
elif age >=65:
    print("$5")

#测试多个条件
a=['mushrooms','cheese']
if 'mushrooms' in a:
    print("mushrooms")
if 'haha' in a:
    print("haha")
if 'cheese' in a:
    print("cheese")

for b in a:
    if b=='mushrooms':
        print("oooo")
    else:
        print(b)

#确定列表不是空的
c=[]
if c:
   for d in c:
       print("sssssss")
else:
    print("fffff")      


#使用多个列表
a=['z','x','c','g','v']  
b=['z','d','c'] 
for b1 in b:
    if b1 in a:
        print("b1")
    else:
        print("sorry")

#字典,键值对
alien_0={'color':'green','points':5}
print(alien_0['color'])
new_points=alien_0['points']
print(str(new_points))#转化为字符串
#添加键值对
alien_0['x_potion']=0
print(alien_0)

#创建空字典
alien_0={}
alien_0['color']='green'
#修改字典中的值
alien_0['color']='yellow'

#对一个能够以不同速度移动的外星人的位置进行跟踪
#存储外星人的当前速度，并确定该外星人将向右移动多远
alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("原始x-posion："+str(alien_0['x_position']))
#向右移动外星人
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print("新x-posion："+str(alien_0['x_position']))

#删除键值对
alien_0={'color':'green','points':5}
del alien_0['points']
print(alien_0)

#由类似对象组成的字典
#调查4个人，询问他们最喜欢的编程语言是什么
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    }
print(favorite_languages['sarah'].title())

#遍历所有键值对
for key,value in favorite_languages.items():
    print(key.title()+":"+value.title())
  
#遍历字典中的所有键
for key in favorite_languages.keys():
    print(key.title())

#按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(name.title())

#遍历字典中的所有值
for key in favorite_languages.values():
    print(key.title())
#去重复的值，找出列表中国独一无二的元素
for key in set(favorite_languages.values()):
    print(key.title())

#嵌套
#字典列表
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#创建一个外星人空列表
aliens=[]
#创建30个绿色的外星人
for alien_number in range(30):
    new_alien={'color':'green','points':5}
    aliens.append(new_alien)

#显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
print("总共:"+str(len(aliens)))

for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']='20'
for alien in aliens[:5]:
    print(alien)
print("...")
print("总共:"+str(len(aliens)))

#在字典中存储列表
pizza={
    'crust':'trick',
    'toppings':['mushrooms','cheese']
}
print(pizza['crust'])
for topping in pizza['toppings']:
    print("\t"+topping)

#在字典中存储字典
#多个网站用户，每个用户都有自己独特的用户名，字典里用户名为键，
users ={
    'asinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }
for username,user_info in users.items():
    print(username)
    full_name=user_info['first']+" "+user_info['last']
    location=user_info['location']
    print(full_name.title())
    print(location.title())

#用户输入
#message=input("tell me sth,and i will repeat it back:")
#print(message)

prompt="if you tell us who you are"
prompt += "\nwhat is your first name?"
#name = input(prompt)
#print("hello,"+name)

#获取数值输入
#age=input("how old are you")
age= int(age)
if age>=12:
    print("haha")

#求模运算符（余数）---------失败
5%3   #2

#使用while循环
current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1

#让用户选择何时退出
prompt ="enter 'q' to end"
message=""
while message!='q':
    message=input(prompt)
    if message!='q':
        print(message)

#使用标志
prompt ="enter 'q' to end"
active=True
while active:
    message=input(prompt)
    if message=='q':
        active=False
    else:
        print(message)

#使用break退出循环
while True:
    message=input(prompt)
    if message=='q':
        break
    else:
        print(message)

#在循环中使用continue
current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)

#避免无限循环
#x=1
#while x<=5:
  #  print(x)

#在列表之间移动元素
#创建一个待验证用户列表，和一个用于存储已验证用户的空列表
unconfirmed_usrs=['alice','brain','candace']
confirmed_users=[]

while unconfirmed_usrs:
    current_user =unconfirmed_usrs.pop()
    confirmed_users.append(current_user)
for confirmed_user in confirmed_users:
    print(confirmed_user)

#删除包含特定值的所有列表元素
pets=['a','b','a','c','d',]
while 'a' in pets:
    pets.remove('a')
print(pets)

#使用用户输入来填充字典
responses={}
polling_active=True
while polling_active:
    name=input("your name")
    response = input("your moutain")
    #将答案存储在字典中
    responses[name]=response
    repeat=input("haha")
    if repeat=='no':
        polling_active=False
for name ,response in responses.items():
    print(name + " "+response)

#定义函数
def greet_user():
    print("hello")
greet_user()

#向函数传递信息
def greet_user(username):
    print("hello:"+username)
greet_user('jesse')

#传递实参：1、位置实参
def describe_pet(animal_type,pet_name):
    print(animal_type+"'s name is "+pet_name)
describe_pet('hamster','harry')

#关键字实参，不一定要位置正确
def describe_pet(animal_type,pet_name):
    print(animal_type+"'s name is "+pet_name)
describe_pet(animal_type='hamster',pet_name='harry')

#默认值，没有指定实参时，用形参的默认值，必须按顺序
def describe_pet(pet_name,animal_type='dog'):
    print(animal_type+"'s name is "+pet_name)
describe_pet(pet_name='harry')

#返回值
def get_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()

musician=get_name('jimi','hendrix')
print(musician)

#让实参变成可选的
def get_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=first_name+' '+middle_name + ' '+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()

musician=get_name('jimi','hendrix')
print(musician)

#返回字典
def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('jimi','hendrix')
print(musician)

#结合使用函数和while循环
def get_name(first_name,last_name,middle_name=''):
    full_name=first_name+' '+last_name
    return full_name.title()
while True:
    print("enter q at any time to quit")
    f_name=input("first name:")
    if f_name=='q':
        break
    l_name=input("last name:")
    if l_name=='q':
        break
    full_name=get_name(f_name,l_name)
    print(full_name)    

#传递列表
def greet_users(names):
    for name in names:
        msg="hello, "+name.title()
        print(msg)
usernames=['a','b','c']
greet_users(usernames)

#在函数中修改列表，修改是永久性的
#为用户提交的设计制作3d打印模型的公司，需要打印的设计存储在一个列表中，
#打印后移到另一个列表中
#不用函数
#unprinted_designs=['a','b','c']
#completed_models=[]
#while unprinted_designs:
#    current_design=unprinted_designs.pop()
#    completed_models.append(current_design)
#for completed_model in completed_models:
#    print(completed_model)

#用函数
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        completed_models.append(current_design)
def show_completed_modes(completed_models):
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs=['a','b','c']
completed_models=[]
print_models(unprinted_designs,completed_models)
show_completed_modes(completed_models)

#禁止函数修改列表
#向函数传递列表的副本
#function_name(list_name[:])

#传递任意数量的实参
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('a')
make_pizza('a','b','c')

def make_pizza(*toppings):
    for topping in toppings:
        print("---"+topping)
make_pizza('a')
make_pizza('a','b','c')

#结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
    for topping in toppings:
        print("---"+topping)
make_pizza(16,'pepper')
make_pizza(12,'mushroom','green peppers')

#使用任意数量的关键字实参,两个*可以创建一个名为user_info的空字典
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含有关用户的一切"""
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile =build_profile('a','b',location='c',filed='d')

print(user_profile)

#将函数存储在模块中
# 导入整个模块，见其他文件

#根据类创建对象被称为实例化
#创建和使用类
#创建一个表示小狗的类dog
#包含名字和年龄+蹲下和打滚
#使用类去创建表示特地小狗的示例
#创建dog示例时，通过实参向dog（）传递名字和年龄，self会自动传递（不用自己传递）

class Dog():
    def __init__(self, name ,age):
        """初始化属性name和age,创建一个示例时会自动运行该函数"""
        #以self为前缀的变量都可供类中的所有方法使用
        #获取存储在形参name中的值，并将其存储到变量name中，然后该变量被关联到当前创建的示例
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+" is now setting")

    def roll_over(self):
        print(self.name.title()+" rolled over")

#访问属性：根据类创建示例,my_dog.name获取属性的值
my_dog=Dog('willie',6)
print("my dog's name is "+my_dog.name.title())
print("my dog is "+str(my_dog.age))
#调用方法
my_dog.sit()
my_dog.roll_over()
#创建多个示例
your_dog=Dog('lucy',3)

class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性，制造商型号年份"""
        self.make =make
        self.model=model
        self.year=year
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
my_car=Car('audi','a4','2016')
print(my_car.get_descriptive_name())

#给属性指定默认值
#odometer_reading,属性，初始值为0
#read_odometer(),方法
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性，制造商型号年份"""
        self.make =make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("this car has "+ str(self.odometer_reading)+" miles")

my_car=Car('audi','a4','2016')
print(my_car.get_descriptive_name())
my_car.read_odometer()

#修改属性的值
#1、直接修改属性的值
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性，制造商型号年份"""
        self.make =make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("this car has "+ str(self.odometer_reading)+" miles")

my_car=Car('audi','a4','2016')
print(my_car.get_descriptive_name())
my_car.odometer_reading=23
my_car.read_odometer()

#2、通过方法修改属性的值
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性，制造商型号年份"""
        self.make =make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("this car has "+ str(self.odometer_reading)+" miles")
    def update_odometer(self,mileage):
        if mileage>= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer")

my_car=Car('audi','a4','2016')
print(my_car.get_descriptive_name())
my_car.update_odometer(24)
my_car.read_odometer()

#3、通过方法对属性的值递增
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性，制造商型号年份"""
        self.make =make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("this car has "+ str(self.odometer_reading)+" miles")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
    def update_odometer(self,mileage):
        if mileage>= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer")

my_car=Car('audi','a4',2016)
print(my_car.get_descriptive_name())
my_car.update_odometer(235)
my_car.read_odometer()
my_car.increment_odometer(100)
my_car.read_odometer()

#继承，子类继承父类的所有属性和方法，同时还可以定义自己的属性和方法
#子类的方法init（）
class ElectricCar(Car):
    def __init__(self,make,model,year):
        """初始化父类的属性,super把父类和子类关联起来"""
        super().__init__(make,model,year)
my_tesla=ElectricCar('tesla','model s', 2016)
print(my_tesla.get_descriptive_name())

#给子类定义属性和方法
class ElectricCar(Car):
    def __init__(self,make,model,year):
        """初始化父类的属性,再初始化电动汽特有的属性"""
        super().__init__(make,model,year)
        self.battery_size=70
    def describe_battery(self):
        print("this car has a "+str(self.battery_size)+" battery")
my_tesla=ElectricCar('tesla','model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#重写父类的方法，用的子类的

#将实例用作属性
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=70
    def describe_battery(self):
        print("this car has a "+str(self.battery_size)+" battery")


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
    
my_tesla=ElectricCar('tesla','model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()