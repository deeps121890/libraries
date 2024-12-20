'''
import pandas as pd
data={
    'Name':['Alice','Bob','Charlie'],
    'Age':[30,21,29],
    'City':['Banglore','Tamil nadu','kerela']
}
print(pd.DataFrame(data))
'''
o/p;
Name  Age        City
0    Alice   30    Banglore
1      Bob   21  Tamil nadu
2  Charlie   29      kerela
'''
import pandas as pd
details={
    'Department_Name':['DS','ECE','CSE','EEE','Mech'],
    'HOD':['prasad','Ramesh','Suresh','Harish','Sathish'],
    'Percentage':[92.8,90.3,87.6,99.2,89.7]
}
print(pd.DataFrame(details))
'''
o/p:
Department_Name      HOD  Percentage
0              DS   prasad        92.8
1             ECE   Ramesh        90.3
2             CSE   Suresh        87.6
3             EEE   Harish        99.2
4            Mech  Sathish        89.7
'''
import pandas as pd
data=[10,20,30,40]
series=pd.Series(data,index=['a','b','c','d'])
print(series)
'''
o/p:
a    10
b    20
c    30
d    40
dtype: int64
