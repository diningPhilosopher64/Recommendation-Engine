import sys 
import recsys
import recsys.algorithm
from recsys.algorithm.factorize import SVD
from recsys.algorithm.factorize import SVDNeighbourhood
from recsys.datamodel.data import Data
from recsys.evaluation.prediction import RMSE,MAE
import numpy as np
import pandas as pd
recsys.algorithm.VERBOSE = True
movies_file = "/media/sourabhkondapaka/Sourabh's/main_project/sandbox/ml-latest-small/movies.csv"
movies = pd.read_table(movies_file, sep=',')
movies.columns = ['movie_id','title','genres']
ratings_file = "/home/sourabhkondapaka/Desktop/ratingsss.csv"





class Collaborative_filtering(object):
    def __init__(self,ratings_file,movies):#No need to pass as ,will be provided in views.py
        #self.users = users
        self.movies = movies
        self.K = 100
        self.PERCENT_TRAIN = 85
        #Need to provide a default file location for ratings.csv instead of loading everytime.run below 2lines only once 
        #or just provide this file instead.
        #self.users.to_csv("/home/sourabhkondapaka/Desktop/ratingsss.csv",index= False)
        self.ratings_file = ratings_file  #Give your path to ratings.csv created from above 2 lines.
        self.data = None
        self.svd = None
        self.recommend_movies_list = None
        self.recommend_movies_ids = None
        self.similar_movies_list = None
        self.similar_movies_ids = None
        
        self.movie_id = None
        self.train = None
        self.test = None

        
        
    def compute_svd(self):      
        self.data = Data()
        self.data.load(self.ratings_file, sep=',', format={'col':0, 'row':1 ,'value':2, 'ids':float})
        self.train , self.test = self.data.split_train_test(percent=self.PERCENT_TRAIN)    
        self.svd = SVDNeighbourhood()
        self.svd.set_data(self.train)    
        self.svd.compute(k=self.K, min_values=1, pre_normalize=None, mean_center=True, post_normalize=True)

    def similarity_measure(self,movie1 , movie2): #gives a similarity measure value between -1 to 1
        return round(self.svd.similarity(movie1,movie2),4)
    
    def recommend_movies(self,user_id):
        l =  self.svd.recommend(user_id, n=10, only_unknowns=True, is_row=False)
        self.recommend_movies_list = []
        self.recommend_movies_ids = []
        for p in l:
            #movie names
            bb = str(movies.ix[movies['movie_id'] == p[0] ]['title']).split()    
            q = bb.index('Name:')
            bb = ' '.join(bb[1:q])
            self.recommend_movies_list.append(bb) 
            #movie ids
            gg = movies.ix[movies['movie_id'] == p[0]]
            gg = gg.reset_index()
            del gg['index']
            gg = gg.ix[:,0:2].as_matrix(columns = None).tolist()
            self.recommend_movies_ids.append(gg[0][0])
        return self.recommend_movies_list,self.recommend_movies_ids
    
    def get_similar_movies(self,movie1):#Returns a PYTHON list for similar movies.
        l = self.svd.similar(movie1)
        self.similar_movies_list = []
        self.similar_movies_ids = []
        l = l[2:]
        
        for p in l:
            #getting movie names
            bb = str(movies.ix[movies['movie_id'] == p[0] ]['title']).split()    
            q = bb.index('Name:')
            bb = ' '.join(bb[1:q])
            self.similar_movies_list.append(bb)   
            #getting movie id's
            self.similar_movies_ids.append(p[0])
            
        return self.similar_movies_list,self.similar_movies_ids
    