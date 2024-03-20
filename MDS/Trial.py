
import requests
import pandas as pd
import numpy as np
df = pd.read_excel('//Users//mukund//Desktop//trial.xlsx')

df = df.replace({np.nan: ''})
data_list = []

for index,row in df.iterrows():

    data_dict = {
        "firstname": row["firstname"],
        "lastname": row ["lastname"]
    }

    data_list.append(data_dict)
    data_dict_str = str(data_dict)

    df.at[index, 'result'] = data_dict_str

payload = {"data": data_list}

df.to_excel('modified_excel_file.xlsx', index=False)

print(data_dict)