import  pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
#df = pd.read_csv("genome-scores-20m.csv")
#df =df.pivot(values="relevance",index="movieId",columns="tagId")
#df =pd.DataFrame(cosine_similarity(df,df))
#df.to_pickle("MovieSimMatrix.pkl")
#print(df)
#df = pd.read_csv("movies-20m.csv")
#df = df.set_index ( "movieId")

""""
#df.to_pickle("movies-20m.pkl")
df = pd.read_csv("genome-scores-20m.csv")
l = list(set(df['movieId']))
df = pd.read_pickle("MovieSimMatrix.pkl")
df.columns = l
df.index = l
print(df)
df.to_pickle("MovieSimMatrix.pkl")
"""
df = pd.read_csv("genome-scores-20m.csv")
a = list(set(list(df['movieId'])))
a.sort()
df =df.pivot(values="relevance",index="movieId",columns="tagId")
df =pd.DataFrame(cosine_similarity(df,df))
df.columns = a
df.index = a
df.to_pickle("MovieSimMatrix.pkl")
print(df)