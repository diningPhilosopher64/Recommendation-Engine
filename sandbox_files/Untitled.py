import numpy as np
import pandas as pd

import math as mt
import csv
from sparsesvd import sparsesvd 
import numpy as np
from scipy.sparse import csc_matrix 
from scipy.sparse.linalg import * 

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


movielens = pd.merge(users , movies)


user_ratings_matrix = users.pivot_table(values = "rating", index = "user_id", columns = "movie_id")



MAX_PID = 671
MAX_UID = 9066


def computeSVD(urm, K):
    U, s, Vt = sparsesvd(urm, K)
    dim = (len(s), len(s))
    S = np.zeros(dim, dtype=np.float32)
    for i in range(0, len(s)):
        S[i,i] = mt.sqrt(s[i])
    U = csc_matrix(np.transpose(U), dtype=np.float32)
    S = csc_matrix(S, dtype=np.float32)
    Vt = csc_matrix(Vt, dtype=np.float32)
    
    return U, S, Vt





#Used in SVD calculation (number of latent factors)
K=100

#Initialize a sample user rating matrix
urm = user_ratings_matrix
urm = csc_matrix(urm, dtype=np.float32)

#Compute SVD of the input user ratings matrix
U, S, Vt = computeSVD(urm, K)


print (U.shape)
