import pandas as pd
df =pd.read_csv("data.csv",index_col="order_id")
##selection By column 
print(df.loc["1001":"B005",["unit_price"]])