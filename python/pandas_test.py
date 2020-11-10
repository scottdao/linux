from pandas import Series,DataFrame
import pandas as pd
# obj = Series([4,5,6,-7])
# print(obj)
# print(obj.index)
#

# print(obj.values)

# --> index
# obj2 = Series([4,7,3,1], index=['a', 'b', 'c', 'd'])
# print(obj2)


# obj2['a'] = 7
# print(obj2)

# print('a' in obj2)

#$data = {
 #       'beijing':1233,

#}

data = {
        'city':['shanghai', 'beijing', 'beijing', 'shanghai', 'shenzhen'],
        'year':[2016, 2018, 2017, 2020, 2019],
        'pop': [1.5, 1.6, 1.9, 2.0, 1.4]
        }

frame = DataFrame(data)
# print(frame)


# entry index

frame2 = DataFrame(data, columns=['year','city','pop'])
# print(frame2)
#print(frame2['city'])

#print(frame2.city)
frame2['new'] = 100
frame2['cap'] = frame2.city == 'beijing'
# print(frame2)




### dataFrame index row and col  exchange

pop = {
         'beijing':{2008:1.5, 2020:2},
         'shanghai':{2008:2, 2020:1.8}
        }

frame3 = DataFrame(pop)
# print(frame3.T) # col row exchange (x.T)
obj6 = Series(['blue', 'purple', 'yellow'], index=[0,3,5])
#print(obj6.reindex(range(6), method='bfill'))

from numpy import nan as NA
data = Series([[1, NA, 2],[1,2,NA], ['13', NA, 9]])
#print(data.dropna(how='all'))

data.fillna(0)
print(data.fillna(0, inplace=True))
print(data)
