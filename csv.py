'''
import pandas as pd
data={'Name':['deepika','deena'],
       'Age':[21, 56],
        'City':['banglore','dubai']}
df=pd.DataFrame(data)
df['Pho_num']=[371873283, None]
print(df)
df.loc[1,'Pho_num']=123456789
print(df)
df=pd.read_csv('employees.csv')
print(df)
df.to_csv('employees.csv',index=False)
#Reading data from CSV file
import pandas as pd
data={'Name':['deepika','deena'],
       'Age':[21, 56],
        'City':['banglore','dubai']}
df_csv=pd.DataFrame(data)
df_csv['Pho_num']=[371873283, None]
print(df_csv)
df_csv.loc[1,'Pho_num']=123456789
print(df_csv)
df_csv.to_csv('employees.csv')
print(df_csv)
df_csv=pd.read_csv('employees.csv')
print(df_csv)
'''
o/p:
Name  Age      City      Pho_num
0  deepika   21  banglore  371873283.0
1    deena   56     dubai          NaN
      Name  Age      City      Pho_num
0  deepika   21  banglore  371873283.0
1    deena   56     dubai  123456789.0
      Name  Age      City      Pho_num
0  deepika   21  banglore  371873283.0
1    deena   56     dubai  123456789.0
   Unnamed: 0     Name  Age      City      Pho_num
0           0  deepika   21  banglore  371873283.0
1           1    deena   56     dubai  123456789.0

