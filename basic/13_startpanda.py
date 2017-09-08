#-*- coding: utf-8 -*-
# Numpy 是列表形式的，没有数值标签，而 Pandas 就是字典形式。Pandas是基于Numpy构建的
# Panda 資料結構: Series and DataFrame

import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])
# np.nan == None
# 索引在左边，值在右边。由于我们没有为数据指定索引。于是会自动创建一个0到N-1（N为长度）的整数型索引。

print(s)
"""
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
"""

print "************* DataFrame 的创建 *************"
dates = pd.date_range('20160101', periods=6)
print dates
'''
DatetimeIndex(['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04',
               '2016-01-05', '2016-01-06'],
              dtype='datetime64[ns]', freq='D')
'''
#生成6*4的數列，值是任意生成，index為直行，是dates
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])

print(df)
"""
                   a         b         c         d
2016-01-01 -0.253065 -2.071051 -0.640515  0.613663
2016-01-02 -1.147178  1.532470  0.989255 -0.499761
2016-01-03  1.221656 -2.390171  1.862914  0.778070
2016-01-04  1.473877 -0.046419  0.610046  0.204672
2016-01-05 -1.584752 -0.700592  1.487264 -1.778293
2016-01-06  0.633675 -1.414157 -0.277066 -0.442545
"""

df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
# 沒有指定index跟Column會自動從0~n-1生成index
print(df1)

"""
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
"""
print "************* 用字典代替我們要輸入的值 *************"
#
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print df2
print df2.dtypes
print df2.index   # Int64Index([0, 1, 2, 3], dtype='int64')
print df2.columns # Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
# df2.values 可以只印出值，df2.describe()可印出數字總結例如平均值等等
"""
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""

# 按照index值大小排序
print(df2.sort_index(axis=1, ascending=False))
"""
     F      E  D    C          B    A
0  foo   test  3  1.0 2013-01-02  1.0
1  foo  train  3  1.0 2013-01-02  1.0
2  foo   test  3  1.0 2013-01-02  1.0
3  foo  train  3  1.0 2013-01-02  1.0
"""

# 按照某列的直排序
print(df2.sort_values(by='B'))
"""
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""

print "************* 選擇數據 *************"
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

"""
             A   B   C   D
2013-01-01   0   1   2   3
2013-01-02   4   5   6   7
2013-01-03   8   9  10  11
2013-01-04  12  13  14  15
2013-01-05  16  17  18  19
2013-01-06  20  21  22  23
"""

#可以選取A column的值
print df['A']
print df.A

print df[0:3], df['20130102':'20130104']
#0~3行的項目,   還有'20130102'~'20130104'列的項目

print "************* loc *************"

print(df.loc['20130102'])
# 通过标签名字选择某一行数据， 或者通过选择某行或者所有行（:代表所有行）然后选其中某一列或几列数据

print(df.loc[:, ['A', 'B']])
"""
             A   B
2013-01-01   0   1
2013-01-02   4   5
2013-01-03   8   9
2013-01-04  12  13
2013-01-05  16  17
2013-01-06  20  21
"""

print(df.loc['20130102', ['A', 'B']])
"""
A    4
B    5
Name: 2013-01-02 00:00:00, dtype: int64
"""

print "************* iloc *************"


