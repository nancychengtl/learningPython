#-*- coding: utf-8 -*-
import numpy as np
#calcuation of numpy is based on array
array = np.array([[1, 2, 3],
                  [2, 3, 4]])#2x3 matrix
print (array) #使用, 區分
print ('number of dim:', array.ndim) #array的維度
print ('shape of matrix:', array.shape)
print ('size of array', array.size) #在array中全部elements數目

array1 = np.array([1, 2, 3], dtype=np.int64) #定義array中的type
#np.float64, float32, int32 (space used will be smaller in 32 than in 64)
print (array1.dtype)

a = np.zeros((3, 4), dtype = np.int16) #generate an 3x4 array with 0s
print (a)

b= np.arange(10, 20, 2)
#generate an array starting from 10 to 20 with a interval of 2
print (b)

c = np.arange(12).reshape((3, 4))
#generate an array starting from 0 to 11 with shape of 3X4

d = np.linspace(1, 10, 5)
#generate an array of 5 lines between 1 to 10
print (d)

e = np.array([10, 20, 30, 40])
f = np.arange(4)

print (e, f)
g = e + f
h = e**2 #square of e
i = 10*np.sin(e) #sin of e
print (g)
print (i)
print (e < 3) #print elements smaller than 3 => [False False False False]

m1 = np.array([[1, 1],
                [0, 1]])

m2 = np.arange(4).reshape((2, 2))
#[[0 1]
#[2 3]]
m3 = m1*m2
m3_dot = np.dot(m1, m2)
m3_dot_2 = m1.dot(m2) #result is as same as m3_dot
print (m2)
print (m3)
print (m3_dot)

#randomly gerenate an array
print (np.random.random((2, 4)))
print (np.sum(m2)) #sum((m2) axis = 1)search in row
print (np.min(m2)) #min((m2) axis = 0)search in column
print (np.max(m2))

n1 = np.arange(2, 14).reshape((3, 4))
print (np.argmin(n1)) #minium of index
print (np.argmax(n1)) #maxium of index
print (np.mean(n1))
# = print (n1.mean(n1))

print (np.cumsum(n1)) #add elements to sum iteratively
print (np.diff(n1)) #diff between 2 elements nearby
print (np.sort(n1)) #sort for each row
print (np.transpose(n1)) #= (n1.T)
print (np.clip(n1, 5, 9)) #the elements > 9 is replaced by 9, the elements < 5 is replaced by 5

n2 = np.arange(3, 15)
print (n2) #[ 3  4  5  6  7  8  9 10 11 12 13 14]
print (n2[3]) #6

n2 = np.arange(3, 15).reshape((3,4))
"""
[[ 3  4  5  6]
 [ 7  8  9 10]
 [11 12 13 14]]
 
 print(n2[2]) => [11 12 13 14]
 print(n2[2][1]) = print(n2[2, 1])=> 12
"""
print(n2[1, 1:3])#[8 9]

for row in n2:
    print (row)
for column in n2.T:
    print (column)

print "********************  merge  *****************************"

p1 = np.array([1, 1, 1]) #is not a matrix, therefore can not be transposed
p2 = np.array([2, 2, 2])
print (np.vstack((p1, p2)))
# [[1 1 1]
#  [2 2 2]]

print (np.hstack((p1, p2))) #[1 1 1 2 2 2]

A = np.array([1, 1, 1])[:, np.newaxis]
print (np.shape(A)) #(3, 1)
"""
[[1]
 [1]
 [1]]
"""
B = np.array([2, 2, 2])[:, np.newaxis]
"""
[[2]
 [2]
 [2]]
"""

C = np.vstack((A, B))  # vertical stack
D = np.hstack((A, B))  # horizontal stack

print(D)
"""
[[1 2]
[1 2]
[1 2]]
"""

print(A.shape, D.shape)
# (3,1) (3,2)

C = np.concatenate((A, B, B, A), axis=0)

print(C)
"""
array([[1],
       [1],
       [1],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [1],
       [1],
       [1]])
"""

D = np.concatenate((A, B, B, A), axis=1)
print(D)
"""
array([[1, 2, 2, 1],
       [1, 2, 2, 1],
       [1, 2, 2, 1]])
"""

print "********************  split  *****************************"

A = np.arange(12).reshape((3, 4))
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""
print (np.split(A, 2, axis=1)) # 垂直的切成兩個split vertically into 2 parts
"""
[[0, 1],    [[ 2,  3],
[4, 5],     [ 6,  7],
[8, 9]]     [10, 11]]
"""
print (np.array_split(A, 3, axis=1))
print (np.vsplit(A, 3))
#[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
print (np.hsplit(A, 2))

print "********************  copy  *****************************"

# 用 "=" 會使得矩陣相互關聯
# 在賦值的狀態下改變任意一個其中的矩陣中的值, 其他a, b, c 矩陣的值也會同時改變
a = np.arange(4)
b = a
c = a
d = b
a[0] = 11
print (b is a) #True

d[1:3] = [22, 33]   # array([11, 22, 33,  3])
# 在賦值的狀態下改變任意一個其中的矩陣中的值, 其他a, b, c 矩陣的值也會同時改變

# 如果使用 copy 則不會有值相互影響的問題
b = a.copy()    # deep copy
print(b)        # array([11, 22, 33,  3])
a[3] = 44
print(a)        # array([11, 22, 33, 44])
print(b)        # array([11, 22, 33,  3])
