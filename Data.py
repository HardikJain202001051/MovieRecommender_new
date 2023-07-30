#genome = pd.read_csv("genome-scores-20m.csv").pivot(index="movieId", columns="tagId")
#ids = genome.index.tolist()
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import scipy.sparse as sp
import sklearn.preprocessing

from sklearn.neighbors import NearestNeighbors
""""
genome = pd.read_csv("genome-scores-20m.csv")
genome=genome.pivot(index="movieId",columns="tagId")
ids = genome.index.tolist()
similarity_matrix = pd.DataFrame(cosine_similarity(genome, genome), index=ids)
similarity_matrix.columns = ids
print(similarity_matrix)
#similarity_matrix.to_pickle("Content_SimMatrix.pkl")
"""
""""
ratings = pd.read_csv("ratings-20m.csv")
ratings=ratings.pivot(index="movieId",columns="userId")
ids = ratings.index.tolist()
ratings.fillna(0,inplace=True)
similarity_matrix = pd.DataFrame(cosine_similarity(ratings, ratings), index=ids)
similarity_matrix.columns = ids
#print(similarity_matrix)
ratings =csr_matrix(ratings.values)
#print(ratings)
similarity_matrix = pd.DataFrame(cosine_similarity(ratings, ratings), index=ids)
similarity_matrix.columns = ids
print(similarity_matrix)
"""
ratings = pd.read_csv("ratings-20m.csv")
ratings=ratings.pivot(index="movieId",columns="userId")
ids = ratings.index.tolist()
ratings.fillna(0,inplace=True)
similarity_matrix = pd.DataFrame(cosine_similarity(ratings, ratings), index=ids,columns=ids)
similarity_matrix.index.rename="movieId"
print(similarity_matrix)
#csr_rating = pd.DataFrame(csr_rating,index=ids)
#csr_rating.columns =ids
#similarity_matrix.to_pickle("Collab_SimMatrix.pkl")
#print(pd.DataFrame(similarity_matrix,index=ids,columns=ids))

