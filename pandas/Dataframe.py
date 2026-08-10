import pandas as pd
data ={"Name": ["Ram","shyam","gita"],
       "Age":[30,35,50]
       }

df = pd.DataFrame(data,index =["employee 1","employee 2","...."])

##add new column

df["Job"]=["cook","N/A","cashier"]

#add new row
new_row =pd.DataFrame([{"Name":"sandy","age":29,"Job":"engineer"}],indec=["employee 4"])
df =pd.concat([df,new_row])
print(df)