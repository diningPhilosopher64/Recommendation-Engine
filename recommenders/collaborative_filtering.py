import sys 
import recsys
import recsys.algorithm
from recsys.algorithm.factorize import SVD
from recsys.datamodel.data import Data
import pandas as pd
from recsys.evaluation.prediction import RMSE,MAE
recsys.algorithm.VERBOSE = True


#These paths are to be given by Irfan 

#users_file = "/media/sourabhkondapaka/Sourabh's/main_project/sandbox/ml-latest-small/ratings.csv"
#movies_file = "/media/sourabhkondapaka/Sourabh's/main_project/sandbox/ml-latest-small/movies.csv"
#users = pd.read_table(users_file,sep=',', header=None,names = ['user_id','movie_id','rating','timestamp'],index_col = False)
#movies = pd.read_table(movies_file, sep=',')


class collaborative_filtering():
    def __init__(self, users , movies):
        self.users = users
        self.movies = movies    
        movies = movies
        self.K = 100
        self.PERCENT_TRAIN = 85
        self.users.to_csv("/home/sourabhkondapaka/Desktop/ratingsss.csv",index= False)
        self.ratings_file = "/home/sourabhkondapaka/Desktop/ratingsss.csv"
        self.data = None
        self.svd = None
        self.movie_list = None
        self.train = None
        self.test = None

        
        
    def compute_svd(self):      
        selfdata = Data()
        data.load(ratings_file, sep=',', format={'col':0, 'row':1 ,'value':2, 'ids':float})
        train , test = data.split_train_test(percent=PERCENT_TRAIN)    
        self.svd = SVD()
        self.svd.set_data(train)    
        self.svd.compute(k=K, min_values=1, pre_normalize=None, mean_center=True, post_normalize=True)
