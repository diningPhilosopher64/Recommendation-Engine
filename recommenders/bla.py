import popularity_based 
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



pb = popularity_based(users,movies)

pb.create()

movies = pb.recommend()

