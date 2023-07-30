import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
import time
start_time = time.time()
class MovieRecommender():

    def __init__(self,name,max_id,watchlist):
        self.content_similiarity_matrix_df = pd.read_pickle(self.name+"Content_SimMatrix.pkl")
        self.collaborative_similiarity_matrix_df = pd.read_pickle(self.name+"Collab_SimMatrix.pkl")
        #self.movies_df = pd.read_csv("movies-20m.csv")
        #self.ratings_df= pd.read_csv("ratings-20m.csv")
        self.name = name
        self.id = max_id+1
        self.watchlist_name = "Watchlist_" + self.name + ".csv"
        #watchlist = pd.DataFrame(watchlist,columns = "ratings" ,index = "movieId")

    def lookup_movie_id_by_title(movie_title):
        print(movies[movies.title.str.contains(movie_title)])

    def Content_Recommender(self):
        Mat = self.name+"Content_SimMatrix.pkl"
        similar_items = pd.DataFrame(self.content_similiarity_matrix_df.loc[find_movie_similiar_to])
        similar_items.columns = ["content_similarity_score"]
        similar_items = similar_items.sort_values('content_similarity_score', ascending=False)
        similar_items = similar_items.head(10)
        similar_items.reset_index(inplace=True)
        similar_items = similar_items.rename(index=str, columns={"index": "movieId"})
        similar_movies_content = pd.merge(self.movies_df, similar_items, on="movieId")
        self.similar_movies_content = similar_movies_content
        return similar_movies_content

    def Collab_Recommender(self):
        find_movie_similiar_to = int(input("Enter the id of the movie :"))
        similar_items = pd.DataFrame(self.collaborative_similiarity_matrix_df.loc[find_movie_similiar_to])
        similar_items.columns = ["collab_similarity_score"]
        similar_items = similar_items.sort_values('collab_similarity_score', ascending=False)
        similar_items = similar_items.head(10)
        similar_items.reset_index(inplace=True)
        similar_items = similar_items.rename(index=str, columns={"index": "movieId"})
        similar_movies_collab = similar_items
        similar_movies_collab = pd.merge(self.movies_df, similar_movies_collab, on="movieId")
        similar_movies_collab = similar_movies_collab.sort_values('collab_similarity_score', ascending=False)
        self.similar_movies_collab = similar_movies_collab
        return similar_movies_collab

    def Hybird_Recommender(self):
        find_movie_similiar_to = int(input("Enter the id of the movie :"))
        similar_items = pd.DataFrame(self.content_similiarity_matrix_df.loc[find_movie_similiar_to])
        similar_items.columns = ["content_similarity_score"]
        similar_items = similar_items.sort_values('content_similarity_score', ascending=False)
        similar_items = similar_items.head(10)
        similar_items.reset_index(inplace=True)
        similar_items = similar_items.rename(index=str, columns={"index": "movieId"})
        similar_movies_content = pd.merge(self.movies_df, similar_items, on="movieId")

        similar_items = pd.DataFrame(self.collaborative_similiarity_matrix_df.loc[find_movie_similiar_to])
        similar_items.columns = ["collaborative_similarity_score"]
        similar_items = similar_items.sort_values('collaborative_similarity_score', ascending=False)
        similar_items = similar_items.head(10)
        similar_items.reset_index(inplace=True)
        similar_items = similar_items.rename(index=str, columns={"index": "movieId"})
        similar_movies_collab = similar_items
        similar_movies_collab = pd.merge(self.movies_df, similar_movies_collab, on="movieId")
        similar_movies_collab = similar_movies_collab.sort_values('collaborative_similarity_score', ascending=False)

        similiar_hybrid_df = pd.merge(similar_movies_collab, pd.DataFrame(similar_movies_content['content_similarity_score']), left_index=True, right_index=True)
        similiar_hybrid_df['average_similarity_score'] = (similiar_hybrid_df['content_similarity_score'] + similiar_hybrid_df['collaborative_similarity_score']) / 2
        similiar_hybrid_df.drop("collaborative_similarity_score", axis=1, inplace=True)
        similiar_hybrid_df.drop("content_similarity_score", axis=1, inplace=True)
        similiar_hybrid_df.sort_values('average_similarity_score', ascending=False, inplace=True)
        return similiar_hybrid_df


    def add_to_watchlist(self,watchlist):
        user_Content_matrix = pd.read_pickle(self.name+"Content_SimMatrix.pkl")
        user_Content_matrix = pd.read_pickle("Content_SimMatrix.pkl").loc[ : , list(watchlist.keys())]
        for i in watchlist.keys():
            user_Content_matrix[i] = user_Content_matrix[i].apply(lambda x: x * watchlist[i])
        user_Content_matrix['mean'] = user_Content_matrix.mean(axis = 1)
        user_Content_matrix = user_Content_matrix['mean']
        user_Content_matrix = user_Content_matrix.drop(watchlist.keys())
        user_Content_matrix = user_Content_matrix.sort_values(ascending=False)
        user_Content_matrix = user_Content_matrix.head(50)
        user_Content_matrix.to_pickle(self.name+"Content_SimMatrix.pkl")
        user_Content_matrix = None

        Collab_Matrix = pd.read_pickle("Collab_SimMatrix.pkl")
        for i in watchlist.keys():
            Collab_Matrix[i][self.id] = watchlist[i]
        ids = Collab_Matrix.rows.tolist
        Collab_Matrix = pd.DataFrame(cosine_similarity(user_rating), index=ids)
        Collab_Matrix.columns = ids
        user_rating = pd.read_pickle(self.name+"Collab_SimMatrix.pkl")
        user_rating = Collab_Matrix.loc[ : , list(watchlist.keys())]
        Collab_Matrix = None
        user_rating.to_pickle(self.name+"Collab_SimMatrix.pkl")
        user_rating = None


print("--- %s seconds ---" % (time.time() - start_time))








    

