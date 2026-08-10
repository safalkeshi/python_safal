import pandas as pd
calories = {"Day 1": 1760,"Day 2": 2100," day 3" :1770}
series = pd.Series(calories)
print(series.loc["day 4"])