
import numpy as np
import pandas as pd

# set some print options
np.set_printoptions(precision=4)
np.set_printoptions(threshold=5)
np.set_printoptions(suppress=True)
pd.set_option('precision', 3, 'notebook_repr_html', True, )
# init random gen
np.random.seed(2)



users_file = "/media/sourabhkondapaka/Sourabh's/main_project/sandbox/ml-latest-small/ratings.csv"
movies_file = "/media/sourabhkondapaka/Sourabh's/main_project/sandbox/ml-latest-small/movies.csv"
users = pd.read_table(users_file,sep=',', header=None,names = ['user_id','movie_id','rating','timestamp'])
movies = pd.read_table(movies_file, sep=',')



class popularity_based():
    def __init__(self,users,movies):
        self.users = users
        self.movies = movies
        self.user_id = None
        self.mean_ratings = None
        self.movielens= None
        self.c  = 0

    def create(self):
        self.movielens = pd.merge(self.users,self.movies)
        self.movie_ratings = self.movielens.ix[:,1:3]
        self.mean_ratings = self.movie_ratings.groupby('movie_id',as_index = True)['rating'].mean().sort_values(ascending = False)
        self.mean_ratings = pd.DataFrame(self.mean_ratings).reset_index()
        self.mean_ratings['title'] = self.mean_ratings['movie_id'].map(self.movies.set_index('movie_id')['title'])

    def recommend(self,topu): #no arguement required here, just for the sake of uniformness across other recommender implementations
        self.user_id = user_id
        #From = self.c
        #self.c += topu
        #To = self.c        
        return self.mean_ratings.ix[:topu,'title'].as_matrix(columns = None)




