import sys 
import recsys
import recsys.algorithm
from recsys.algorithm.factorize import SVD
from recsys.algorithm.factorize import SVDNeighbourhood
from recsys.datamodel.data import Data
import pandas as pd
import numpy as np
import csv

ratings_file = "/home/sourabhkondapaka/Desktop/ratingsss.csv"
ratings = pd.read_csv("/home/sourabhkondapaka/Desktop/ratingsss.csv",index_col= False)

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
        movie_id = int(movie_id)
        rating_value = float(rating_value)
        bla = [user_id,movie_id,rating_value,665345]
        
        if check_user(user_id):
            print "user exists"
            pc = ratings.movie_id[ratings.user_id == user_id]  # gets all the movies rated by this user
            ad = pc.tolist()
            for a in ad:
                print a
            if movie_id < ad[-1]: #user_id == get_last_user_id() and
                print "user exists and not the last row in the filtered table"
                s = 0
                # This loop finds the exact location in the table to store the rating.
                for p in ad:
                    if movie_id < p:
                        s =  ad.index(p)
                        break
                seperate = pc[pc == ad[s]]
                seperation = seperate.index[0]            
                top_half = ratings[:seperation]
                lower_half = ratings[seperation:]
                top_half.loc[len(top_half)] = bla
                top_half.index = top_half + 1
                top_half = top_half.append(lower_half,ignore_index = True)
                top_half.to_csv("/home/sourabhkondapaka/Desktop/ratingsss.csv",index = False)  
            else:
                print "user exists and is the last row in the filtered table"
                seperate = pc[pc == ad[len(ad) - 1]] 
                seperation = seperate.index[0]            
                top_half = ratings[:seperation + 1]
                lower_half = ratings[seperation + 1:]
                top_half.loc[len(top_half)] = bla
                top_half.index = top_half + 1
                top_half = top_half.append(lower_half,ignore_index = True)
                top_half.to_csv("/home/sourabhkondapaka/Desktop/ratingsss.csv",index = False)  
                    
        else:
            print "user does not exist"
            ratings.loc[len(ratings)] = bla
            ratings.to_csv("/home/sourabhkondapaka/Desktop/ratingsss.csv",index = False) 


def rated_movies(user_id): # Gets all the movies rated by a particular user.
    pc = ratings.movie_id[ratings.user_id == user_id]
    return pc.tolist()




