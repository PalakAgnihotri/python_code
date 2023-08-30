# pandas is a python lirary used for working with data sets . pandas allow us to analyze big data and make concluson ased on statistical theories.
# why use? pandas can clean messy data sets and make them readable and relevant.
# in series,data frame work
# pyhton data analysis
# what do? pandas give you answers about is there relation between rows and columns,max value,min value etc.and give result with past data.

import pandas as pd


# a=[10,'ab',30,'computer']
# mycol=pd.Series(a)
# print(mycol)
# print(mycol[1])
# print(type(mycol))

# CREATING OWN INDEX

# b=[15,25,35]
# s=pd.Series(b,index=['x','y','z'])
# print(s)

# CREATING SERIES THROUGH AN ARRAY

# import pandas as pd
# import numpy as np
# data=np.array([5,6,7,8])
# ds=pd.Series(data,index=[10,20,30,40])
# print(ds)

# creating a series through a dictionary

# dict={"a":10,"b":20,"c":30}
# ds=pd.Series(dict)
# print(ds)

#  creating a series through a dictionary using fewer keys as index

# dict={"a":10,"b":20,"c":30}
# ds1=pd.Series(dict,index=["a","b",1])
# ds2=pd.Series(dict,index=["p","q",1])
# print(ds1)
# print(ds2)

# creating 

# dict={"a":10,"b":20,"c":30}
# print(pd.Series(dict,index=["a","b","c","a","b","c"]))

# Creating series using numpy

# import numpy as np
# ds=pd.Series(np.ones(10))
# print(ds)
# ds1=pd.Series(np.arange(12,25))
# print(ds1)

# CREATING DATAFRAME FROM THREE SERIES(LIST)/DICTIONARY LIST:

# data={
#     "names":['Abhishek','harsh','nikhil'],
#     "roll no":[100,101,102],
#     "marks":[90,88,85]
# }
# df=pd.DataFrame(data)
# print(df)

# ASSIGNING INDEX

# df=pd.DataFrame(data,index=["st1","st2","st3"])
# print(df)

# Accessing a column
# print(df["marks"])

# print(df["marks"]['st1'])

# print(df[0:2]['names'])

# Creating dataframes using numpy arrays

# import numpy as np
# npar=np.array([['abc','xyz','uvw'],[101,102,103],[90,88,85]])
# np_dict={'names':npar[0],'roll no':npar[1],'marks':npar[2]}
# df=pd.DataFrame(np_dict)
# print(df)
# df3=df['roll no'][1]
# print(df3)

# list_of_list=[['abc',101,109],['xyz',102,88],['uvw',103,85]]
# df4=pd.DataFrame(list_of_list,columns=['names','roll no','marks'])
# # df4=pd.DataFrame(list_of_list)
# print(df4)

# list_of_list=[
#     {'names':'abc','roll no':101,'marks':90},
#     {'names':'xyz','roll no':102,'marks':88},
#     {'names':'uvw','roll no':103,'marks':85}
# ]
# df=pd.DataFrame(list_of_list)
# print(df)

# creating df using series of dictionary

# s1=pd.Series(['xyz','abc','uvw'])
# s2=pd.Series([101,102,103])
# s3=pd.Series([90,88,85])
# dict_of_series={'names':s1,"roll no":s2,"marks":s3}
# df=pd.DataFrame(dict_of_series)
# print(df)

# fetching data from excel

# df=pd.read_excel(r"C:\Users\agnih\OneDrive\student.xlsx")
# print(df)
# print(df.head())# by default only 5 will shown
# print(df.tail())# by default only 5 will shown
# print(df.loc[0])
# print(df.loc[0:4])
# print(df.loc[4,'name'])
# print(df.loc[0:5,['name','roll no']])

# print(df.iloc[0:4,0:2])
            #row,column 
# in i location we put purely index and it work as range,but in location we put full location

# inner join : is like intersection of data frames based on a column
# merge() function is used for merging dfs
# st={"roll no":[1,2,3,4],'name':['ram','sita','ran','tan']}
# df1=pd.DataFrame(st)
# sts={'roll no':[1,2,3,4],'marks':[20,30,40,50]}
# df2=pd.DataFrame(sts)
# rst=pd.merge(df1,df2)#inner merging 
# print(st)
# print(sts)
# print(rst)

# Inner will only work when anything is common in both data frames 

# st={'name':['ram','sita','ran','tan'],"rollno":[1,2,3,4]}
# df1=pd.DataFrame(st)
# sts={'name':['dfg','ram','sdf','fgc'],'marks':[20,30,40,50]}
# df2=pd.DataFrame(sts)
# rst=pd.merge(df1,df2,on='name',how='inner',indicator=True)
# print(rst)

# outer will run with bot common and uncommon

# rst=pd.merge(df1,df2,on='name',how='outer',indiactor=True)
# print(rst)

#  how(left side table full information and right side only matched)

# rst=pd.merge(df1,df2,on='name',how='left',indiactor=True)
# print(rst)

# how(left side table full information and right side only matched)

# rst=pd.merge(df1,df2,on='name',how='right',indicator=True)
# print(rst)

# AGGREGATION=IT IS A FUNCTION USED TO APPLY SOME AGGREGATION ACROSS ONE OR MORE COLUMNS FREQUENTLY USED FUNCTIONS: SUM,MIN,MAX,MIN,COUNT)

# st={'name':['ram','sita','ran','tan'],"rollno":[1,2,3,4]}
# df1=pd.DataFrame(st)
# sts={'name':['dfg','ram','sdf','fgc'],'marks':[20,30,40,50]}
# df2=pd.DataFrame(sts)
# print(df1.rollno.count())
# print(df1.rollno.max())
# print(df1.rollno.min())
# print(df1.rollno.sum())
# import numpy as np

# dfg=pd.DataFrame({'A':['foo','bar','foo','bar','bar','foo','foo','bar','foo'],'B':['one','one','one','two','three','two','three','one','two'],'C':np.random.randint(2,9,size=(9,)),'D':np.random.randint(10,16,size=(9,))})
# print(dfg)

# groupby() is used to create groups among entries of DF based on values in a column

# g=dfg.groupby('A')
# print(g)

# g.groups() to check the groups inside groupy data frame

# print(g.groups)

# iterating through the groups df

# for i,j in g:
#     print(i)
    # print(j)

