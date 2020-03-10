import pizza


#导入特定的函数
#from pizza import make_pizza#就不要写前面的pizza

#使用as给函数知道别名
#from pizza import make_pizza as mp
#mp(16,'peper')

#给模块别名
#import pizza as p
#p.make_pizza(16,'peper')
#导入所有函数
#from pizza import *
#make_pizza(16,'peper')
pizza.make_pizza(16,'peper')
pizza.make_pizza(12,'mushroom','green pepers')