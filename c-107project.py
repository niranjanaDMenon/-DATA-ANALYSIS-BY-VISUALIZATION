import pandas as pd 
import plotly.express as px 

df = pd.read_csv("data analysis master.csv")

print(df.groupby("level")["attempt"].mean())

mean = df.groupby(["Sudent ID","Level"],as_index = False)["attempt"].mean()

fig = px.scatter()x=df.groupby("level")["attempt"].mean(),y=["Level1","Level2","Level3","Level4"],orientation="h"))
fig.show()