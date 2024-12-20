'''
import pandas as pd
data = {'Name': ['deepika', 'deena'],
        'Age': [21, 56],
        'City': ['banglore', 'dubai']}
df_json = pd.DataFrame(data)
# Add a new column 'Pho_num'
df_json['Pho_num'] = [371873283, None]
print(df_json)
# Update 'Pho_num' for row 1
df_json.loc[1, 'Pho_num'] = 123456789
print(df_json)
df_json.to_json('employees.json', orient='records', lines=True)
# Read data from the saved JSON file
df_json_read = pd.read_json('employees.json', orient='records', lines=True)
print(df_json_read)
'''
o/p:
      Name  Age      City      Pho_num
0   deepika   21  banglore  371873283.0
1     deena   56     dubai          NaN
      Name  Age      City      Pho_num
0   deepika   21  banglore  371873283.0
1     deena   56     dubai  123456789.0
{"Name":"deepika","Age":21,"City":"banglore","Pho_num":371873283.0}
{"Name":"deena","Age":56,"City":"dubai","Pho_num":123456789.0}
      Name  Age      City      Pho_num
0   deepika   21  banglore  371873283.0
1     deena   56     dubai  123456789.0

