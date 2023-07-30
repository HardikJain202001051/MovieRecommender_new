import pandas as pd

d = pd.read_csv("links-20m.csv")
d.index = d["movieId"]
d = d["imdbId"]
print(d)

a  = pd.read_pickle("Content_SimMatrix.pkl")
a.index
a["imdbId"] = d
a.index = a["imdbId"]
a.drop(["imdbId"],inplace=True,axis=1)
a.columns = a.index
print(a)
