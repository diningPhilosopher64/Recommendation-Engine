import sys 
import recsys
import recsys.algorithm
from recsys.algorithm.factorize import SVD
from recsys.algorithm.factorize import SVDNeighbourhood
from recsys.datamodel.data import Data
import pandas as pd
import numpy as np
import csv


# use this when you need fresh ratngsss.csv
#users.to_csv("/home/sourabhkondapaka/Desktop/ratingsss.csv",index= False)

#ratings.csv declared in the original file itself.

#Gets value of last user_id required during registration

def get_last_user_id():
    la = ratings['user_id'].iloc[-1]
    return la

def check_user(user_id): # Returns true if user already exists.
    if  any(ratings['user_id'] == user_id):
        return True
    else:
        return False


def rate_movie(user_id , movie_id , rating_value):
    pc = ratings.movie_id[ratings.user_id == user_id]  # gets all the movies rated by this user
    ad = pc.tolist() #converts to list
    s = 0
    # This loop finds the exact location in the table to store the rating.
    for p in ad:
        if movie_id < p:
            s =  ad.index(p)
            break
    #Splits the table at this point.
    seperate = list(pc[pc == s].index)[0]
    #The row which will be added to the table.
    bla = [user_id,movie_id,rating_value,665345]
    #Splitting the table
    pq = ratings[:seperate+1]
    rs = ratings[seperate+1:len(ratings)]
    pq.loc[len(pq)] = bla
    pq.index = pq.index + 1
    pq = pq.append(rs , ignore_index=True)
    pq.to_csv("/home/sourabhkondapaka/Desktop/ratingsss.csv",index = False)


def rated_movies(user_id): # Gets all the movies rated by a particular user.
    pc = ratings.movie_id[ratings.user_id == user_id]
    return pc.tolist()


