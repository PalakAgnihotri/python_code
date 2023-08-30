# NUMERICAL PYTHON
import numpy as np
# import sys
# arr1=np.array([1,2,3,4],dtype='int8')
# print(arr1)
# print(type(arr1))
# print(sys.getsizeof(arr1))
# list1=[1,232323,3,4,5]
# print(list1)
# print(type(list1))
# print(sys.getsizeof(list1))

# 1 D ARRAY 

# import numpy as np
# arr1=np.array([1,4,7,9,5,6],np.int32)
# print(arr1)
# print(arr1.dtype)# data type of each element    
# print(arr1.ndim)# number of dimension
# print(arr1.itemsize)# size in bytes of each element
# print(arr1.nbytes)# sizes in bytes of whole array
# print(arr1.size)# number of elements
# print(arr1.shape)#order of array 

# 2 D array
# import numpy as np
# arr2=np.array([[1,2,3],[4,5,6]],"int8")
# print(arr2)
# # print(arr2[0,1])
# print(arr2.dtype)# data type of each element    
# print(arr2.ndim)# number of dimension
# print(arr2.itemsize)# size in ytes of each element
# print(arr2.nbytes)# sizes in bytes of whole array
# print(arr2.size)# number of elements
# print(arr2.shape)#order of array 

# 3D ARRAY

# import numpy as np
# arr2=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,0,1],[0,0,1],[1,0,0]]],"int64")
# print(arr2)
# print(arr2.dtype)# data type of each element    
# print(arr2.ndim)# number of dimension
# print(arr2.itemsize)# size in bytes of each element
# print(arr2.nbytes)# sizes in bytes of whole array
# print(arr2.size)# number of elements
# print(arr2.shape)#order of array 

# # QUESTION
# import numpy as np
# arr1=np.array([12,34,56,78,3,5,2,7,8,9,11,10,15])
# print(arr1)
# print(arr1[3:10])# start=3,stop=10
# print(arr1[3:])# start=3
# print(arr1[:8])# start=0,stop=8
# print(arr1[-9:-2])# start=-9,stop=-2
# print(arr1[2:11:3])# start=2,stop=11,step=3
# print(arr1[10:4:-1])# start=10,stop=4,step=-1
# print(arr1[::-1])# reverse of array

# SLICING 2D ARRAY

import numpy as np
# arr2=np.array([[4,8,12,1,3],[6,8,11,2,6],[-1,6,7,8,9],[2,7,8,1,7]])
# print(arr2)
# print(arr2[1:3,2:4])
# print(arr2[-2:-1,-4:-2])
# print(arr2.ndim)
# print(arr2.shape)

# USING ARANGE() FUNCTION
# it creates only 1D array

# import numpy as np
# arr2=np.arange(4,12)
# print(arr2)
# arr3=np.arange(10,30,4)
# print(arr3)

# RESHAPE
# arr1=np.arange(15)
# print(arr1)
# arr4=arr1.reshape(3,5)# in reshape row*column(3*5=15)=original array
# print(arr4)
#RESIZE
# arr1=np.arange(15)
# print(arr1)
# arr1.resize(2,3)# in reshape row*column(3*5 not equal to 15)=original array
# print(arr1)

# a1=np.empty((3,5))
# print(a1)
# a2=np.zeros((3,5))
# print(a2)
# a3=np.ones((2,5,3))
# print(a3)
# a4=np.identity(3)
# print(a4)
# a5=np.eye(3,4)
# print(a5)
# a6=np.linspace(1,5,4)
# print(a6)
# a7=np.linspace(0,2*np.pi,100)
# print(a7)
# b=np.sin(a7)
# print(b)
# a8=np.arange(9)
# print(a8)
# a9=np.empty_like(a8)
# print(a9)
# a9[4]=200
# print(a9)
# print(a8)
# a10=np.arange(12).reshape(3,4)
# print(a10)
# a11=np.ravel(a10)
# print(a11)
# a11[4]=200
# print(a11)
# print(a10)
# a12=np.arange(12).reshape(3,4)
# print(a12)
# a13=a12.flatten()
# print(a13)
# a13[4]=200
# print(a12)
# print(a13)
# a14=np.diag([4,7,12])
# print(a14)
# a15=np.arange(10,15).reshape(3,3)
# print(a15)
# a16=np.random.randint(2,10,size=(3,5,2))
# print(a16)

# REPLICATING BY SLICING
# IT CREATES VIEW OF THE ARRAY
# a17=np.arange(5,17).reshape(3,4)
# print(a17)
# b=a17[2:,1:3].copy()
# print(b)
# b[0][1]=200
# print(b)
# print(a17)

# JOINING TWO ARRAYS
# Hstack
# Vstack
# block


# Hstack=Horizontal stacking
# a18=np.arange(6,12).reshape(2,3)
# print(a18)
# a19=np.arange(8).reshape(2,4)
# print(a19)
# a20=np.hstack([a19,a18])
# print(a20)

# Vstack=Vertical stacking
# a21=np.arange(6,12).reshape(2,3)
# print(a21)
# a22=np.arange(12).reshape(4,3)
# print(a22)
# a23=np.vstack([a21,a22])
# print(a23)

# Block
# a24=np.array([1,2,3,4])
# a25=np.array([5,6,7,8])
# a26=np.array([9,10,11,12])
# a27=np.array([13,14,15,16])
# e=np.block([[a24,a25],[a26,a27]])
# print(e)

# QUESTION

# a=np.identity(2)
# b=np.zeros((2,2))
# c=np.diag([7,8])
# d=np.eye(2,2)
# e=np.block([[a,b],[c,d]])
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# SPLIT(list of sub arrays)
# a=np.arange(15)
# b=np.split(a,5)# (list of sub arrays)
# print(a)
# print(b)

# a=np.arange(34,49)
# b=np.split(a,[3,5,10,13])
# print(a)
# print(b)
# for arr in b:
#     print(arr.sum())

# IN 1D array

# SUM

# a1=np.array([12,56,23,11])
# print(a1)
# print(a1.sum())

# MAX()

# a1=np.array([12,56,23,11])
# print(a1)
# print(a1.max())

# MIN()

# a1=np.array([12,56,23,11])
# print(a1)
# print(a1.min())

# INDEX OF MAXIMUM VALUE

# a1=np.array([12,56,23,11])
# print(a1)
# print(a1.argmax())

# INDEX OF MINIMUM VALUE

# a1=np.array([12,56,23,11])
# print(a1)
# print(a1.argmin())

# ARRANGING INDEX IN ASSCENDING ORDER WITH RESPECT TO NUMBERS

# a1=np.array([12,56,23,11])
# print(a1)
# print(a1.argsort())

# SORT(VALUES IN ASSCENDING ORDER)

# a1=np.array([12,56,23,11])
# print(a1)
# print(a1.sort())

# MEAN ,VARIANCE,STANDARD DEVIATION

# a1=np.array([12,56,23,11])
# print(a1)
# print(a1.mean())
# print(a1.var())
# print(a1.std())

# IN 2D ARRAY

# SUM IN 2D

# a1=np.arange(10,19).reshape(3,3)
# print(a1)
# print(a1.sum())
# print(a1.sum(axis=0))# column wise
# print(a1.sum(axis=1))# row wisea1=np.arange(10,19).reshape(3,3)

# MAX IN 2D

# a1=np.array([[23,56,12,11],[7,3,1,61]])
# print(a1)
# print(a1.max())
# print(a1.max(axis=0))# column wise
# print(a1.max(axis=1))# row wise

# INDEX OF MAXIMUM VALUE IN 2D

# a1=np.array([[23,56,12],[7,3,61],[8,4,9]])
# print(a1)
# print(a1.argmax())
# print(a1.argmax(axis=0))# column wise
# print(a1.argmax(axis=1))# row wise

# SORTING IN 2D (ALWAYS ROW WISE)

# a1=np.array([[23,56,12],[7,3,61],[8,4,9]])
# print(a1)
# print(a1.sort())
# print(a1)

# a1=np.array([[1,6,7],[2,5,3],[1,5,8]])
# print(a1)
# print(a1+5)
# print(a1-3)
# print(a1*4)
# print(a1/5)
# print(a1//2)
# print(a1%2)
# print(a1**3)
# print(a1**0.5)

# TRANSPOSE OF MATRIX

# a1=np.arange(6).reshape(3,2)
# print(a1)
# print(a1.T)

# ADDITION OF TWO MATRICES

# a1=np.arange(6).reshape(2,3)
# a2=np.array([[12,6,5],[11,8,23]])
# print(a1)
# print(a2)
# print(a1+a2)
# print(np.add(a1,a2))

# SUBTRACTION OF TWO MATRICES

# a1=np.arange(6).reshape(2,3)
# a2=np.array([[12,6,5],[11,8,23]])
# print(a1)
# print(a2)
# print(a1-a2)
# print(np.subtract(a1,a2))

# MULTIPLY

# a1=np.arange(6).reshape(2,3)
# a2=np.array([[12,6,5],[11,8,23]])
# print(a1)
# print(a2)
# print(a1*a2)# element wise multiplication not the manually type so we should not use it
# print(np.multiply(a1,a2))

#  DOT (IT IS USED FOR MULTIPLICATION)

# a1=np.arange(6).reshape(2,3)
# a2=np.array([[1,2],[2,1],[-1,1]])
# print(a1)
# print(a2)
# a3=np.dot(a1,a2)
# print(a3)

# P A N D A S
# P A N D A S
# P A N D A S
# P A N D A S
# P A N D A S
# P A N D A S
# P A N D A S


# a1 = np.array([[1,6,7],[2,5,3],[1,5,8]])
# print(a1)
# print(a1 + 5)
# print(a1 - 3)
# print(a1*4)
# print(a1/5)
# print(a1//2)
# print(a1%2)
# print(a1**3)
# print(a1**0.5)
# x = np.random.random((5,5))
# print("Original Array:")
# print(x)
# print(x.shape)
# print(x.dtype)# data type of each element    
# # print(arr1.ndim)# number of dimension
# print(x.itemsize)# size in bytes of each element
# # print(arr1.nbytes)# sizes in bytes of whole array
# print(x.size)# number of elements