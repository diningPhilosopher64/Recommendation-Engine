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

movies.columns = ['movie_id','title','genres']

movielens = pd.merge(users , movies)

movie_ratings = movielens.ix[:,1:3]

gg = movie_ratings.groupby('movie_id', as_index=True)['rating'].mean().sort_values(ascending=False)
gg = pd.DataFrame(gg).reset_index()


gg['title'] = gg['movie_id'].map(movies.set_index('movie_id')['title'])



pq = gg.ix[:3,'title'].as_matrix(columns= None)


pp = gg.sort(['movie_id'],ascending=True)

pp = pp.ix[:,0:2]

pp = pp.reset_index()

del pp['index']




pp.to_csv("/home/sourabhkondapaka/Desktop/bla.csv")

