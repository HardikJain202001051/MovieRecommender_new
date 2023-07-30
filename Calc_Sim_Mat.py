import pandas as pd
def Content_Recommender():
    n = int(input("Enter number of movies : "))
    dict = {}
    for i in range(n):
        movieid =  int(input("Enter movie ID : "))
        rating =  float(input("Enter rating between 2.5 and 5 : "))
        if rating>2.5:
            dict[movieid] = rating
    keys = dict.keys()
    user_Content_matrix = pd.read_pickle("MovieSimMatrix.pkl").loc[:, keys]
    #print(user_Content_matrix)
    for i in keys:
        user_Content_matrix[i] = user_Content_matrix[i].apply(lambda x: x * dict[i])
    user_Content_matrix['mean'] = user_Content_matrix.mean(axis=1)
    user_Content_matrix = user_Content_matrix['mean']
    user_Content_matrix = user_Content_matrix.sort_values( ascending=False).head(20)
    user_Content_matrix = user_Content_matrix.index.tolist()
    movies = pd.read_pickle("movies-20m.pkl")
    print(user_Content_matrix)
    print(movies.loc[user_Content_matrix])


Content_Recommender()






