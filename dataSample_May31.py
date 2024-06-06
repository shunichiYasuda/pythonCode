import pandas as pd
import numpy as np

obj=pd.Series([4,7,-5,3])
print(obj)
print(obj.values)
print(obj.index)

obj2=pd.Series([4,7,-5,3],index=['d','b','a','c'])
print(obj2)
print(obj2.values)
print(obj2.index)
print(obj2['a'])
print(obj2[['c','d','a']])
print(obj2[obj2>0])
print(obj2[obj2<0])
print(obj2*2)
print(np.exp(obj2))

sdata = {'Ohio':3500,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3 = pd.Series(sdata)
print(obj3)

states = {'California','Ohio', 'Oregon','Texas'}
obj4 = pd.Series(sdata,index=states)
print(obj4)
print(pd.isnull(obj4))
print(obj4.isnull())
print(obj3+obj4)

print(obj4)
#####同じ長さを持つリスト型のバリューを持ったディクショナリ
data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
          'pop':[1.5,1.7,3.6,2.4,2.9,3.2],
          'year':[2000,2001,2002,2000,2001,2002]
        }
frame = pd.DataFrame(data)
print(frame)
frame2 =pd.DataFrame(data,columns=['year','state','pop'],index=['one','two','three','four','five','six'])
print(frame2)
print(frame2['pop'])