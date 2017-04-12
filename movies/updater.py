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
    bla = [user_id,movie_id,rating_value,665345]
    pc = ratings.movie_id[ratings.user_id == user_id]  # gets all the movies rated by this user
    ad = pc.tolist()
    if user_id == get_last_user_id() and movie_id < ad[-1]:
        pc = ratings.movie_id[ratings.user_id == user_id]  # gets all the movies rated by this user
        #print "pc value is",pc,type(pc)         
        ad = pc.tolist() #converts to list
        ad.sort()            
        s = 0
        #finds movie_id less than passed one.
        for p in ad:
            if movie_id < p:
                s =  ad.index(p)
                break            
        seperate = pc[pc == ad[s]]
        #finds location of index to split the table.
        seperation = seperate.index[0]            
        top_half = ratings[:seperation]
        lower_half = ratings[seperation:]
        top_half.loc[len(top_half)] = bla
        top_half.index = top_half + 1
        top_half = top_half.append(lower_half,ignore_index = True)
        top_half.to_csv("/home/sourabhkondapaka/Desktop/ratingsss.csv",index = False)  
    else: #if this happens to be the last row from pc
        pc = ratings.movie_id[ratings.user_id == user_id] 
        ad = pc.tolist() #converts to list
        if movie_id > ad[-1]:
            ratings.loc[len(ratings)]= bla
            ratings.to_csv("/home/sourabhkondapaka/Desktop/ratingsss.csv",index = False)


def rated_movies(user_id): # Gets all the movies rated by a particular user.
    pc = ratings.movie_id[ratings.user_id == user_id]
    return pc.tolist()


