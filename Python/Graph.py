import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# x=[1,2,3]
# y=[9,2,1]
# plt.plot(x,y)
# plt.show()

# x=np.random.randint(1,10,size=5)
# y=np.random.randint(11,20,size=5)
# plt.plot(x,y)
# plt.show()

# x=np.random.randint(1,17,size=5)
# y=[]
# for i in x:
#     y.append(2*i+1)
# plt.plot(x,y,color='green')
# plt.title("motion")
# plt.xlabel("speed")
# plt.ylabel("time")
# plt.show()
# 
#  MULTIPLE GRAPHS

# x=[1,2,3]
# y=[2,4,1]
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("Multiple Graphs")
# plt.plot(x,y,color='green',linestyle=':',label='line1')
# x1=[3,5,6]
# y1=[4,3,2]
# plt.plot(x1,y1,color='black',linestyle=':',label='line2',linewidth=2)
# plt.legend(loc=3)
# plt.show()

# Calculate velocity using v=u+at

# u=20
# a=5
# t=np.arange(2,10)
# v=[]
# for i in t:
#     v.append(u+a*t)
# print(t)
# print(v)

# u=20
# a=5
# t=np.arange(2,21)
# v=[]
# for i in t:
#     v.append(u+a*t)
# print(t)
# print(u)
# plt.xlabel('v')
# plt.ylabel('t')
# plt.plot(v,t)
# plt.show()

# BARGRAPH

# x=np.array(['a','b','c','d'])
# y=np.array(([20,11,35,11]))
# plt.bar(x,y)
# plt.show()

# data=pd.read_excel("C:\\Users\\agnih\\OneDrive\\student.xlsx")
# plt.bar(data['name'],data['roll no'])
# plt.xlabel('name')
# plt.ylabel("roll no")
# plt.show()


# HISTOGRAM

# age=[30,23,34,56,78,33,77,30,456,78,66,73,77,]
# range=(0,100)
# interval=10
# plt.hist(age,interval,range,color='orange')
# plt.xlabel('age')
# plt.ylabel('no. of persons')
# plt.title('age distribution plot')
# plt.show()

# PIECHART using pie()

# revenue=[7267,6785,8765,9876,4567]
# item=['veg','fruits','snacks','drinks','salad']
# plt.pie(revenue,labels=item,wedgeprops={"edgecolor":"yellow"},autopct='%1.1f')
# plt.title("food chart")
# plt.show()

revenue=[7267,6785,8765,9876,4567]
item=['veg','fruits','snacks','drinks','salad']
ex=[0.3,0.3,0.3,0.3,0.3]
plt.pie(revenue,labels=item,wedgeprops={"edgecolor":"yellow"},autopct='%1.1f',explode=ex,startangle=90)
plt.title("food chart")
plt.show()